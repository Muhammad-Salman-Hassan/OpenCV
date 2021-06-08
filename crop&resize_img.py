import cv2
path='F:\open CV\Resources\img.jpg'
img=cv2.imread(path)

cv2.imshow('Lambo',img)
print(f"Shape Before Resizing our image: {img.shape}") #(347, 564, 3) here 347 is height and 564 is width and
# 3 means we have 3 channel of image BGR

#lets resize our image with 500 by 500 px
height,width=500,500 
img_resize=cv2.resize(img,(width,height))
cv2.imshow('Lambo_resize_500X500',img_resize)

#lets resize our image with 600 by 900 px
height,width=600,900
img_resize_600x500 =cv2.resize(img,(height,width))
cv2.imshow("lambo",img_resize_600x500)


#cropping Image
img_cropped=img[:347,50:-1]
cv2.imshow("crop",img_cropped)

cv2.waitKey(0)