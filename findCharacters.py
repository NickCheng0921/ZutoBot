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
import cv2

def recalibrateCharacters(image, color_image):
    #look at image and grab whatever it thinks is a character
    #blur characters with a kernel
    kernel = np.array([[0.5,0.5,1,0.5,0.5],[0.5,1,1,1,0.5],[0.5,1,1,1,0.5],[0.5,1,1,1,0.5],[0.5,0.5,1,0.5,0.5]])
    characters = []
    characterSize = 1000 #pixels for approximate character size
    processed_img = cv2.filter2D(image, -1, kernel)
    #find basic polygons in image https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a
    #                               image         mode  method
    contours, h = cv2.findContours(processed_img,   1,    2)
    #get objects found
    for cnt in contours:
        #approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
        if(cv2.contourArea(cnt) > characterSize):
            #print(cv2.contourArea(cnt))
            Moments = cv2.moments(cnt)
            centerX = int(Moments["m10"] / Moments["m00"])
            centerY = int(Moments["m01"] / Moments["m00"])
            #cv2.drawContours(colored_img,[cnt],0,(randint(1,255), randint(1,255) , randint(1,255)),-1)
            #cv2.fillPoly(colored_img, pts = [approx], color=(255, 0, 0))
            #get average color of character by adding in a 5x5 square around it
            B = G = R = 0
            for i in range(10):
                for j in range(10):
                                   #      Y           X       BGR
                    B += color_image[centerY-5+i][centerX-5+j][0]
                    G += color_image[centerY-5+i][centerX-5+j][1]
                    R += color_image[centerY-5+i][centerX-5+j][2]
            characters.append((centerX, centerY, 0.9*B/100, 0.9*G/100, 0.9*R/100))
            
    return characters
