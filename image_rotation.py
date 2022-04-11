from PIL import Image

img = Image.open("jose.png")

img = img.rotate(angle=50, expand=True, fillcolor="green", resample=Image.BICUBIC, center=(100,100)) # the rotate function takes many arguments like angle, expand and fillcolor which changes the backgroung color and resample parameter which ensure the imgae is of high quality after rotation and it is assigned to bicubic and center of rotation which is set to values

img.show()