import os
import time

import os
from PIL import Image


home_dir = os.path.expanduser('~')
path = os.path.join(home_dir, 'Downloads')

print("Downloads folder path:", path)

tmp = False

def convert(path):
    try:
        webp = Image.open(path)
        png = webp.convert("RGBA")
        png.save(f"{path.replace(".webp",".png")}")
    except:
        pass

while True:
    initial_count = len(os.listdir(path))
    time.sleep(0.2)
    new_count = len(os.listdir(path))
    if tmp:
        new_count += 1
        tmp = False
    if not new_count <= initial_count:
        files = [os.path.join(path, file) for file in os.listdir(path)] # Get the newest file based on modification time 
        new_file = max(files, key=os.path.getmtime)
        print(f"New File: {new_file.replace("\\","/")}")
        if ".webp" in new_file:
            convert(new_file.replace("\\","/"))
            os.remove(new_file.replace("\\","/"))
        if ".tmp" in new_file:
            tmp = True