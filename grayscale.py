from PIL import Image


image = Image.open('mce.jpg').convert('L')

image.show()

image.save('mce_gs.jpg')