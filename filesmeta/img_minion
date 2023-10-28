from PIL import Image
import os


class ImgMinion:
    EX = {"png", "jpg", "jpeg", "gif", "tiff", "bmp", "webp", "svg", "ico"}

    def get_meta_info(self, path):
        metadata = {}
        try:
            if path.split(".")[-1].lower() in self.EX:
                with Image.open(path) as img:
                    width, height = img.size
                    format = img.format
                    mode = img.mode

                metadata = {
                    "Width": width,
                    "Height": height,
                    "Format": format,
                    "Mode": mode,
                }
            return metadata
        except Exception as e:
            return {"error": str(e)}
