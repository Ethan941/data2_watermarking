from PIL import Image
import os

for file_name in os.listdir():
    if ".png" in file_name:
        img = Image.open(file_name)
        img.show() 
