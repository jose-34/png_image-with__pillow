#creating png image
import math
from PIL import Image, ImageDraw
w, h = 300, 300
shape = [(-100, -100), (w - 1, h - 1)] 
# shape1 = [(-100, -100), (w - 100, h - 100)] 
 
img = Image.new('RGB', (w, h), color = 'grey')



img1 = ImageDraw.Draw(img) 
img1.line(shape, fill ="red", width = 0)
# img1.line(shape1, fill = "blue", width = 0)

img.save('pil_red.png')

img.show()
