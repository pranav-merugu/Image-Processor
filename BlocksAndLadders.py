from PIL import Image

image1 = Image.open("pj.jpeg")
image1 = image1.resize((50, 50))
image1.show()