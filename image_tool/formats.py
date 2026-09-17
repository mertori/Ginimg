from .config import FORMAT_MAP

def normalize_format(value):
    value = value.lower()
    if value == "original":
        return "original"
    if value not in {"jpeg", "png", "webp", "avif"}:
        raise ValueError(f"Unsupported output format: {value}")
    return value

def source_format(image):
    fmt = (image.format or "PNG").upper()
    return fmt

def pillow_format(output_format, image):
    if output_format == "original":
        return source_format(image)
    return FORMAT_MAP[output_format]
