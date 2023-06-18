from PIL import Image, ImageEnhance
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


def image_collector():
    Tk().withdraw()
    files = askopenfilenames()
    images = []
    for image in files:
        images.append(image)
    return images

def adjust_image(in_image_path, out_image_path):
    BRIGHTNESS_FACTOR = 1.3
    COLOR_FACTOR = 1.3
    image = Image.open(in_image_path)
    brightness_enhance = ImageEnhance.Brightness(image)
    image = brightness_enhance.enhance(BRIGHTNESS_FACTOR)
    color_enhance = ImageEnhance.Color(image)
    color_enhance.enhance(COLOR_FACTOR).save(out_image_path)

if __name__ == "__main__":
    images = image_collector()
    for image in images:
        image_format_strip = image.strip(".jpg")
        new_name = f"{image_format_strip}_new.jpg"
        adjust_image(image, new_name)