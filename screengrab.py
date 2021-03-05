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
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection of images
    # threshold 1 is high threshold value of intensity gradient
    # threshold2 is low threshold value of intensity gradient
    # takes argument for aperture size for intensity gradient
    processed_img =  cv2.Canny(processed_img, threshold1 = 100, threshold2=300)
    return processed_img

def main():
    print("Running Main")
    last_time = time.time()
    while True:
        #print("running")
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()