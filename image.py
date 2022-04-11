#creating png image
import sys
# import math
from PIL import Image, ImageDraw
w, h = 300, 300

# shape = [(-100, -100), (w - 1, h - 1)] 

# shape1 = [(-100, -100), (w - 100, h - 100)] 
 
img = Image.new('RGB', (w, h), color = 'grey')
img.save('pil_red.png')
with Image.open("pil_red.png") as img:

    # drawing diagonal lines
    draw = ImageDraw.Draw(img)
    draw.line((0, 0) + img.size, fill="red")
    draw.line((0, img.size[1], img.size[0], 0), fill="green")

    # for coloring the triangle formed at the bottom
    draw.polygon([(150, 150), (300, 300), (0, 300)], fill=(0, 0, 255),outline=(0, 0, 0))

     # write to stdout
    img.save(sys.stdout, "PNG")



# img1 = ImageDraw.Draw(img) 
# img1.line(shape, fill ="red", width = 0)
# img1.line(shape1, fill = "blue", width = 0)

img.save('pil_red.png')

img.show()
