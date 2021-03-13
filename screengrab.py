# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:24:28 2021

@author: NuckChead
* https://pythonprogramming.net/open-cv-basics-python-plays-gta-v/?completed=/game-frames-open-cv-python-plays-gta-v/
"""

#import numpy as np
#from PIL import ImageGrab #article details a faster way to do imagegrab
import cv2
import time

from grabScreenFast import grab_screen
from findCharacters import recalibrateCharacters
#get frames
def process_img(image):
    # convert to gray
    #processed_img = image
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection of images
    # threshold 1 is high threshold value of intensity gradient
    # threshold2 is low threshold value of intensity gradient
    # takes argument for aperture size for intensity gradient
    processed_img =  cv2.Canny(processed_img, threshold1 = 100, threshold2= 200)
    #hough lines can detect shape even through some distortions
    #make hough lines detect lines of stages
    # args: input binary image, rho accuracy (distance), radian (step), threshold vote to be line
    # extra args for HoughLinesP: min line length, max gap between line segments
    # step with np.pi/2 for 90 degree steps
    # step with np.pi for 180 degree steps or vertical lines only
    #lines = []
    #lines = cv2.HoughLinesP(processed_img, 1, np.pi/2, 200, 40, 10)
    #draw_lines(processed_img, lines, 3)
 
    #can't draw colored lines onto a binarized image
    #colored_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)
    colored_img = image

    #list of tuples of type (x, y, B, G, R)
    characterList = recalibrateCharacters(processed_img, colored_img)
    #draw ellipses onto characters
    for character in characterList:
        colorSet = (character[2], character[3], character[4])
        print(colorSet[0], colorSet[1], colorSet[2])
        cv2.ellipse(colored_img, (character[0], character[1]), (16,22), 0, 0, 360, colorSet, -1)

    return colored_img

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

def cycles_per_second(timeList):
    res = 0.0
    for i in timeList:
        res += 1.0/i
    res /= len(timeList)
    return res

def main():
    print("Running Main")
    last_time = time.time()
    timeList = [] #list to hold timing for calculation done each frame
    while True:
        #print("running")                         x1   y1   x2    y2
        #screen =  np.array(ImageGrab.grab(bbox=(225, 150, 1125, 600)))
        screen = grab_screen((225, 150, 1125, 600))
        timeList.append(time.time() - last_time)
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print("CPS: ", cycles_per_second(timeList))
            break
main()