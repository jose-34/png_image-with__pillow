from PIL import Image
# we can define file name here
filename =  "resources/services.png"

img = Image.open(filename)

print(img)


img.show()



# def g(x,y,z):
#     print (f'{x+y*z}')

# g("Hi","Hey","Hello")


# lst = []
# i = 0
# while i< 3:
#     lst.insert(i,i)
#     i+=1

# print(lst)


# d = {}
# d[None] = "This is bit tricky!"
# print(d)