#https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent

name = input("Enter file name:")
name += ".png"

from PIL import Image

img = Image.open(name)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    # white
    #if item[0] == 255 and item[1] == 255 and item[2] == 255: 
    #    newData.append((255, 255, 255, 0))
    # purple
    if item[0] == 163 and item[1] == 73 and item[2] == 164:
        newData.append((163, 73, 164, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(name, "PNG")