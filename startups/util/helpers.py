from PIL import Image

def resize_image(image_field, size=(500, 300)):
    if image_field and hasattr(image_field, 'path'):
        img = Image.open(image_field.path)
        img = img.resize(size, Image.LANCZOS)
        img.save(image_field.path)