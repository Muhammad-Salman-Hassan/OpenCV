# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:10:09 2021

@author: sh997
"""

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img)
#img[80:250,300:400]=255,0,0

#cv2.line(img,(55,55),(img.shape[0],img.shape[1]),(255,255,0),10)

cv2.rectangle(img,(150,200),(300,400),(8,95,2),4)
cv2.rectangle(img,(80,180),(300,400),(1,1,3),cv2.FILLED)
cv2.imshow('Image',img)

cv2.waitKey(0)

