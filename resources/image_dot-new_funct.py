from ctypes.wintypes import RGB
from PIL import Image

img = Image.new("RGB",(300,300),(255,100,255))# this function receive mode size and color  arguments(properties)
img.save("jose.png")

img.show()