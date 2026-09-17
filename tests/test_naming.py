from pathlib import Path
from image_tool.naming import build_output_name

def test_compressed_changes_extension():
    result = build_output_name(Path("photo.jpg"), "webp")
    assert result.name == "photo_compressed.webp"

def test_original_filename():
    result = build_output_name(Path("photo.jpg"), "webp", "original")
    assert result.name == "photo.webp"
