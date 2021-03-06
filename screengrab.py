# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:24:28 2021

@author: NuckChead
* set up screen grab for python
* switch to C++ pillow equivalent if this gets slow
* https://pythonprogramming.net/open-cv-basics-python-plays-gta-v/?completed=/game-frames-open-cv-python-plays-gta-v/
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time

#get frames

def process_img(image):
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection of images
    # threshold 1 is high threshold value of intensity gradient
    # threshold2 is low threshold value of intensity gradient
    # takes argument for aperture size for intensity gradient
    processed_img =  cv2.Canny(processed_img, threshold1 = 50, threshold2=100)
    #hough lines can detect shape even through some distortions
    #make hough lines detect lines of stages
    # args: input binary image, rho accuracy (distance), radian (step), threshold vote to be line
    # extra args for HoughLinesP: min line length, max gap between line segments
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 40, 5)
    draw_lines(processed_img, lines)
    return processed_img

def draw_lines(img, lines):
    #draw thicker lines over where we find lines
    for line in lines:
        coords = line[0]
        cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)

def main():
    print("Running Main")
    last_time = time.time()
    while True:
        #print("running")
        screen =  np.array(ImageGrab.grab(bbox=(0,40,1366,768)))
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()