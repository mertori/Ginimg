from pathlib import Path
from PIL import Image

def validate_image(path):
    try:
        with Image.open(path) as im:
            im.verify()
        return True, None
    except Exception as exc:
        return False, str(exc)
