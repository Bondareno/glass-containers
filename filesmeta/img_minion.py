from PIL import Image
from PIL.ExifTags import TAGS
import os


class ImgMinion:
    IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "tiff", "bmp", "webp", "svg", "ico"}

    def get_meta_info(self, path):
        metadata = {}
        try:
            ext = path.split(".")[-1].lower()
            if ext in self.IMAGE_EXTENSIONS:
                with Image.open(path) as img:
                    width, height = img.size
                    format = img.format
                    mode = img.mode

                    # Try to extract additional EXIF data
                    exif_data = self.extract_exif_data(img)

                metadata = {
                    "Width": width,
                    "Height": height,
                    "Format": format,
                    "Mode": mode,
                    "EXIF": exif_data,
                }
            return metadata
        except Exception as e:
            return {"error": str(e)}

    def extract_exif_data(self, img):
        exif_data = {}
        try:
            # Check if the image has EXIF data
            if hasattr(img, "_getexif") and img._getexif() is not None:
                for tag, value in img._getexif().items():
                    tag_name = TAGS.get(tag, tag)
                    exif_data[tag_name] = value
        except Exception as e:
            exif_data = {"error": str(e)}

        return exif_data
