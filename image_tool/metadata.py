from PIL import ImageOps

def prepare_orientation(image):
    return ImageOps.exif_transpose(image)

def remove_metadata(image):
    # Do not copy EXIF/ICC/XMP/info metadata into the new encoded file.
    clean = image.copy()
    clean.info.clear()
    return clean

def exif_present(image):
    try:
        return bool(image.getexif())
    except Exception:
        return False
