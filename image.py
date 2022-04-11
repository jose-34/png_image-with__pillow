#creating png image
import sys
import math
from PIL import Image, ImageDraw
w, h = 300, 300

shape = [(-100, -100), (w - 1, h - 1)] 

# shape1 = [(-100, -100), (w - 100, h - 100)] 
 
img = Image.new('RGB', (w, h), color = 'grey')
with Image.open("pil_red.png") as img:
    draw = ImageDraw.Draw(img)
    draw.line((0, 0) + img.size, fill="red")
    draw.line((0, img.size[1], img.size[0], 0), fill="green")

     # write to stdout
    img.save(sys.stdout, "PNG")



# img1 = ImageDraw.Draw(img) 
# img1.line(shape, fill ="red", width = 0)
# img1.line(shape1, fill = "blue", width = 0)

# img.save('pil_red.png')

img.show()
