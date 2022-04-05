import sys, os
from PIL import Image

def convertImage(path = str):
    file = os.path.splitext(os.path.basename(path))

    # .jpg .jpeg
    if file[1] == ".jpg" or file[1] == ".jpeg":
        input("File already jpg.")
        exit()

    # .webp
    elif file[1] == ".webp":
        img = Image.open(path).convert("RGB")

    # .png    
    elif file[1] == ".png":
        img = Image.open(path).convert("RGB")
    
    else: 
        input("File not image.")
        exit()
    
    img.save(f"{file[0]}.jpg", "jpeg")

try:
    filepath = sys.argv[1] 
    convertImage(filepath)
except IndexError:
    input("File not inputted")
    exit()
