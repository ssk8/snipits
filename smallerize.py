from PIL import Image
import os

"""
    resize jpgs in folder and rotates by EXIF
"""
    
pics = [n for n in os.listdir() if n.endswith(".jpg")]
print(pics)

for pic in pics:
    im = Image.open(pic)
    (width, height) = (im.width // 4, im.height // 4)
    im_resized = im.resize((width, height)) 
    exif = im._getexif()
    if exif[274] == 6:
        im = im.rotate(270, expand=True)
    im.save(f'{pic.removesuffix(".jpg")}_sm.jpg', optimize=True, quality=20)

