import cv2
import  numpy as np


img= cv2.imread("F:\open CV\Resources\pngaaa.com-1825260.png")
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#LPF(low pass filter) helps in removing noise, blurring images, etc. HPF(high path filters) filters help 
# in finding edges in images.
#Adding Gaussian blur to images these are kernels and alpha basically maths behind kernal is he have
# 5X5 matrix of ones
#working:add all the 3 pixels below this kernel, take the average, and replace the central pixel with
#  the new average value. This operation is continued for all the pixels in the image. 

img_blur=cv2.GaussianBlur(img_grey,(5,5),3)

#if you decrease ammount of threshold parameters then it will check more edges
img_canny=cv2.Canny(img_blur,20,20) 

# increasing edge of our canny is called dialtion

kernel=np.ones((5,5),np.uint8)
img_dialtion=cv2.dilate(img_canny,kernel=kernel,iterations=2)



cv2.imshow('shoe',img_grey)
cv2.imshow('shoeblur',img_blur)
cv2.imshow('canny',img_canny)
cv2.imshow('Image_dialation',img_dialtion)

cv2.waitKey(0)
