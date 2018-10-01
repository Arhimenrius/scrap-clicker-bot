import cv2
from PIL import Image
from pyocr.libtesseract import image_to_string
from pyocr.builders import TextBuilder


def detect_text(image_array):
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    pil_image = Image.fromarray(image_array)

    return image_to_string(
        pil_image,
        lang='eng',
        builder=TextBuilder()
    )
