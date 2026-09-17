from image_tool.cli import parse_size

def test_parse_size():
    assert parse_size("500KB") == 500 * 1024
    assert parse_size("1MB") == 1024 * 1024
