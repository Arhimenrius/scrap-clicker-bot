import cv2
import numpy as np


cap = cv2.VideoCapture('tcp://127.0.0.1:5777')

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('hlower', 'result',0,179,nothing)
cv2.createTrackbar('slower', 'result',0,255,nothing)
cv2.createTrackbar('vlower', 'result',0,255,nothing)

cv2.createTrackbar('hupper', 'result',0,179,nothing)
cv2.createTrackbar('supper', 'result',0,255,nothing)
cv2.createTrackbar('vupper', 'result',0,255,nothing)

while(1):

    _, frame = cap.read()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    hlower = cv2.getTrackbarPos('hlower','result')
    slower = cv2.getTrackbarPos('slower','result')
    vlower = cv2.getTrackbarPos('vlower','result')

    hupper = cv2.getTrackbarPos('hupper','result')
    supper = cv2.getTrackbarPos('supper','result')
    vupper = cv2.getTrackbarPos('vupper','result')

    # Normal masking algorithm
    lower_blue = np.array([hlower,slower,vlower])
    upper_blue = np.array([hupper,supper,vupper])
    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()