from __future__ import annotations

import math
import os
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

from .formats import pillow_format
from .metadata import prepare_orientation, remove_metadata

LOSSY = {"JPEG", "WEBP", "AVIF"}

def resize_to_fit(image, max_width=None, max_height=None):
    if not max_width and not max_height:
        return image

    w, h = image.size
    scale = 1.0
    if max_width and w > max_width:
        scale = min(scale, max_width / w)
    if max_height and h > max_height:
        scale = min(scale, max_height / h)

    if scale >= 1:
        return image

    size = (max(1, int(w * scale)), max(1, int(h * scale)))
    return image.resize(size, Image.Resampling.LANCZOS)

def _prepare_for_format(image, fmt):
    image = image.copy()
    if fmt == "JPEG":
        if image.mode in ("RGBA", "LA"):
            bg = Image.new("RGB", image.size, "white")
            alpha = image.getchannel("A")
            bg.paste(image.convert("RGB"), mask=alpha)
            return bg
        if image.mode == "P":
            if "transparency" in image.info:
                rgba = image.convert("RGBA")
                bg = Image.new("RGB", rgba.size, "white")
                bg.paste(rgba.convert("RGB"), mask=rgba.getchannel("A"))
                return bg
            return image.convert("RGB")
        if image.mode != "RGB":
            return image.convert("RGB")
    elif fmt in ("WEBP", "AVIF"):
        if image.mode == "P":
            return image.convert("RGBA" if "transparency" in image.info else "RGB")
    return image

def save_image(image, destination, output_format, quality=80):
    fmt = pillow_format(output_format, image)
    image = _prepare_for_format(image, fmt)

    kwargs = {}
    if fmt == "JPEG":
        kwargs.update(quality=int(quality), optimize=True, progressive=True)
    elif fmt == "WEBP":
        kwargs.update(quality=int(quality), method=6)
    elif fmt == "AVIF":
        kwargs.update(quality=int(quality))
    elif fmt == "PNG":
        kwargs.update(optimize=True, compress_level=9)

    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format=fmt, **kwargs)

def _encode_temp(image, output_format, quality):
    fd, name = tempfile.mkstemp(suffix=".tmp")
    os.close(fd)
    path = Path(name)
    save_image(image, path, output_format, quality)
    return path

def optimize_to_target(image, output_format, target_bytes,
                       remove_exif=True, max_rounds=12):
    fmt = pillow_format(output_format, image)

    if fmt not in LOSSY:
        # Lossless formats cannot use quality to guarantee a target size.
        temp = _encode_temp(image, output_format, 100)
        size = temp.stat().st_size
        return image, None, size, temp, size <= target_bytes

    best = None
    low, high = 1, 100

    while low <= high:
        quality = (low + high) // 2
        temp = _encode_temp(image, output_format, quality)
        size = temp.stat().st_size

        if size <= target_bytes:
            best = (quality, size, temp)
            low = quality + 1
        else:
            temp.unlink(missing_ok=True)
            high = quality - 1

    if best:
        return image, best[0], best[1], best[2], True

    # Quality 1 is still too large: progressively reduce dimensions.
    current = image
    for _ in range(max_rounds):
        w, h = current.size
        new_w = max(320, int(w * 0.85))
        new_h = max(320, int(h * 0.85))
        if (new_w, new_h) == current.size:
            break

        current = current.resize((new_w, new_h), Image.Resampling.LANCZOS)
        low, high = 1, 100
        round_best = None

        while low <= high:
            quality = (low + high) // 2
            temp = _encode_temp(current, output_format, quality)
            size = temp.stat().st_size
            if size <= target_bytes:
                round_best = (quality, size, temp)
                low = quality + 1
            else:
                temp.unlink(missing_ok=True)
                high = quality - 1

        if round_best:
            return current, round_best[0], round_best[1], round_best[2], True

    # Target could not be reached.
    temp = _encode_temp(current, output_format, 1)
    size = temp.stat().st_size
    return current, 1, size, temp, False

def process_image(source, destination, output_format="original", quality=80,
                  target_bytes=None, max_width=None, max_height=None,
                  remove_exif_flag=True):
    with Image.open(source) as original:
        image = prepare_orientation(original)
        image = resize_to_fit(image, max_width, max_height)

        if remove_exif_flag:
            image = remove_metadata(image)

        if target_bytes is not None:
            optimized, chosen_quality, size, temp, reached = optimize_to_target(
                image, output_format, target_bytes, remove_exif=remove_exif_flag
            )
            # Target optimizer already encoded a metadata-clean image.
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(temp, destination)
            return {
                "size": size,
                "quality": chosen_quality,
                "target_reached": reached,
                "width": optimized.width,
                "height": optimized.height,
            }

        save_image(image, destination, output_format, quality)
        return {
            "size": destination.stat().st_size,
            "quality": quality,
            "target_reached": None,
            "width": image.width,
            "height": image.height,
        }
