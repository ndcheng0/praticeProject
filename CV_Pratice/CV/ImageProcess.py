# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 03:07:43 2018

@author: user
"""

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import sys


# matplotlib 顯示圖片
def ShowImg(Image):
    fig = plt.figure("fig_1")
    ax = fig.add_subplot(1, 1, 1)    
    ax.imshow(Image)

def GrayProcess(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def Binarization(image,Value):
    gray = GrayProcess(image)

    ret, temp = cv2.threshold(gray, Value, 255,cv2.THRESH_BINARY_INV)
    temp = cv2.medianBlur(temp, 3)

    return temp
def MappingCnt(cnt):
    area=[]
    for c in cnt:
        area.append(cv2.contourArea(c))
        Mapping(c,2)
    return area

def Mapping(t,value):
    if(value==0):
        for index in range(0,len(t)):
            plt.scatter(t[index][0],-t[index][1],5,'b','s')
    elif(value==1):
        for index in range(0,len(t),2):
            plt.scatter(t[index],-t[index+1],5,'b','s')
    elif(value==2):
        for index in range(0,len(t),2):
            plt.scatter(t[index][0][0],-t[index][0][1],5,'b','s')
def CvShow(Name,Image):
    cv2.namedWindow(Name,cv2.WINDOW_AUTOSIZE)
    cv2.imshow(Name,Image)
    
    while True:
        
        
        
        key = cv2.waitKey(100)
        if key==27:
            print('ESC')
            break
        if cv2.getWindowProperty(Name,0)==-1:
            print('Close')
            break
            
    cv2.destroyAllWindows()

    
        