import os
from PIL import Image
files = os.listdir()
print(files)
img = Image.open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.jfif')
pix_val = list(img.getdata())
print(pix_val)
