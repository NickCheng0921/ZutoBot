# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:06:12 2021

@author: 19259
Text Recognition Using OpenCV's high level API and pre trained models
https://www.docs.opencv.org/master/d9/d1e/tutorial_dnn_OCR.html
Above method is only documented for C++
Try a method of contour finding with python in mind
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time

def recalibrateCharacters(image):
    #blur characters with a kernel
    kernel = np.array([[0.5,0.5,1,0.5,0.5],[0.5,1,1,1,0.5],[0.5,1,1,1,0.5],[0.5,1,1,1,0.5],[0.5,0.5,1,0.5,0.5]])
    processed_img = cv2.filter2D(image, -1, kernel)
    #find basic polygons in image https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a
    #                               image         mode  method
    contours, h = cv2.findContours(processed_img,   1,    2)
    #get objects found
    characters = []
    for cnt in contours:
        #approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
        if(cv2.contourArea(cnt) > 1000):
            print(cv2.contourArea(cnt))
            Moments = cv2.moments(cnt)
            centerX = int(Moments["m10"] / Moments["m00"])
            centerY = int(Moments["m01"] / Moments["m00"])
            #cv2.drawContours(colored_img,[cnt],0,(randint(1,255), randint(1,255) , randint(1,255)),-1)
            #cv2.fillPoly(colored_img, pts = [approx], color=(255, 0, 0))
            characters.append((centerX, centerY))
    return characters
