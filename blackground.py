from PIL import Image
"""
create solid background
"""

(width, height) = (720, 1480)
img = Image.new('RGB', (width, height), color='black') 
img.save(f'background_{height}x{width}.jpg', optimize=True)