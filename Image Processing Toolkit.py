from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import tkinter

img = Image.open("E:\\python\\projects\\PortFolio\\assets\\1.jpg").convert("RGB")
#img.show()
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
    gray = np.dot(image_matrix[..., :3],[0.299,0.587,0.114])
    img_form = Image.fromarray(gray.astype(np.uint8))
    img_form.show()

def Blur(img,value):
    img_form = img.filter(ImageFilter.BoxBlur(value))
    img_form.show()

def Sharpen(img,factor):
    enhancer = ImageEnhance.Sharpness(img)
    img_form = enhancer.enhance(factor)
    img_form.show()

def Resize(img,width,height):
    img_form = img.resize((width, height))
    img_form.show()

def Crop(image_matrix,value_list):
    img_matrix1 = img_matrix[value_list[1]:value_list[0],value_list[3]:value_list[2]]
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Rotate(image_matrix,angle):
    if angle == 90:
        img_matrix1 = np.rot90(img, 1)
    elif angle == 180:
        img_matrix1 = np.rot90(img, 2)
    elif angle == 270:
        img_matrix1 = np.rot90(img, 3)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Flip_Horitontal(img):
    img_matrix1 = np.fliplr(img)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Flip_Vertical(img):
    img_matrix1 = np.flipud(img)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()


#Brightness(img_matrix, 45)  # 0-255
#Contrast(img_matrix, 3)  #0-255
#Invert(img_matrix, 255)  #0-255
#Grayscale(img_matrix)
#Blur(img, 87) # >=0
#Sharpen(img, 9.3)  #real value

#Resize(img, 750, 340)  # >0
#Crop(img_matrix, [100,100,800,500])
#Rotate(img_matrix, 270)  # 90,180,270
#Flip_Horitontal(img)
#Flip_Vertical(img)
