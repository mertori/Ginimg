from pathlib import Path

DEFAULT_INPUT = Path.home() / "workspace/storage/shared/imageCompressor"
DEFAULT_OUTPUT = Path.home() / "workspace/storage/shared/imageCompressed"

FORMAT_MAP = {
    "jpeg": "JPEG",
    "jpg": "JPEG",
    "png": "PNG",
    "webp": "WEBP",
    "avif": "AVIF",
}

INPUT_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".avif",
    ".bmp", ".gif", ".tif", ".tiff"
}
