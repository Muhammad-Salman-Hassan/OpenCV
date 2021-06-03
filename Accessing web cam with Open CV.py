import cv2
import matplotlib.pyplot as plt

#Note if you have one or more webcam you just simple like videoCapture(1,2.....)it is just like your web cam id 

cap = cv2.VideoCapture(0)
framewidth=400
frameheight=100
#Adjusting width and height of our webcam
cap.set(1,framewidth)
cap.set(2,frameheight)

#breaking our web cam loop with press q and 20 sec

while True:
    success,vid=cap.read()
    cv2.imshow("Video",vid)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
