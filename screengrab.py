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

from grabScreenFast import grab_screen

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
    # step with np.pi/2 for 90 degree steps
    # step with np.pi for 180 degree steps or vertical lines only
    lines = []
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/2, 200, 40, 10)
     #draw_lines(processed_img, lines, 3)
    
    #x, contours = cv2.findContours(processed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #can't draw colored lines onto a binarized image
    colored_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)
    draw_red_lines(colored_img, lines, 2)
    cv2.imshow('window', colored_img)

    return processed_img

def draw_lines(img, lines, thickness):
    #draw thicker lines over where we find lines
    for line in lines:
        coords = line[0]
        cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), (255, 255, 255), thickness)

def draw_red_lines(img, lines, thiccy):
    #draw red lines over input
    for line in lines:
        coords = line[0]
        cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), (0, 0, 255), thiccy)

def main():
    print("Running Main")
    last_time = time.time()
    while True:
        #print("running")                        x1 y1 x2 y2
        #screen =  np.array(ImageGrab.grab(bbox=(225, 150, 1125, 600)))
        screen = grab_screen((225, 150, 1125, 600))
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        #cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()