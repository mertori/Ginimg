from pathlib import Path

EXTENSIONS = {
    "jpeg": ".jpg",
    "png": ".png",
    "webp": ".webp",
    "avif": ".avif",
}

def output_extension(output_format, source):
    if output_format == "original":
        ext = source.suffix.lower()
        return ext if ext else ".png"
    return EXTENSIONS[output_format]

def build_output_name(source, output_format, filename_mode="compressed",
                      suffix="_compressed"):
    stem = source.stem
    if filename_mode == "compressed":
        stem += suffix
    return Path(stem + output_extension(output_format, source))

def unique_path(path):
    if not path.exists():
        return path
    i = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{i}{path.suffix}")
        if not candidate.exists():
            return candidate
        i += 1
