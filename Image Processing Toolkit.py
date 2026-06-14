from PIL import Image
import numpy as np

img = Image.open("E:\\python\\projects\\PortFolio\\assets\\1.jpg").convert("RGB")
img.show()
img_matrix = np.array(img)
print(img_matrix.shape)
#a = int(input("Enter choice ="))

def Brightness(image_matrix,value):
    img_matrix1 = value - img_matrix
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Contrast(image_matrix,factor):
    img_matrix1 = np.clip((img_matrix - 128)* factor + 128, 0, 255)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Invert(image_matrix,value):
    img_matrix1 = value - img_matrix
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Grayscale(image_matrix):
    gray = np.dot(img_matrix[..., :3],[0.299,0,587,0.114])
    img_form = Image.fromarray(gray.astype(np.uint8))
    img_form.show()

def Blur(img,value):
    img_form = Img.filter(ImageFilter.BoxBlur(value))
    img_form.show()
