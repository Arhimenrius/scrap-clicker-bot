#!/usr/bin/env python3
import cv2
import numpy as np

def get_video(input_id):
    camera = cv2.VideoCapture(input_id)
    while True:
        okay, frame = camera.read()
        print(okay)
        if not okay:
            break
        print(camera)
        print(frame[300,300])
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #lower_red = np.array([30,30,150])
        #upper_red = np.array([70,70,255])
        #magnetsMask = cv2.inRange(hsv, lower_red, upper_red)
        #res = cv2.bitwise_and(frame,frame, mask= magnetsMask)
        #coordinates = cv2.findNonZero(magnetsMask)
        #if not (coordinates is None):
	    #    for coordinate in coordinates:
	    #    	x = coordinate[0][0]
	    #    	y = coordinate[0][1]
	        	#if((x >= 235 and x <= 405) and (y >= 100 and y <= 370)):
        		#	print(x, y)
        #cv2.imshow('mask',magnetsMask)

        cropped = frame[0:30, 300:350]
        cv2.imshow("cropped", cropped)

        # cv2.imshow('video', frame)
        cv2.waitKey(1)
    pass

if __name__ == '__main__':
    get_video('tcp://127.0.0.1:5777')