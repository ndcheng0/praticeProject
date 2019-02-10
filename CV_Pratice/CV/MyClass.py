# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:51:16 2018

@author: user
"""

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import ImageProcess as ip

class ImgClass:
    threshold=80
    
    def __init__(self,FileName):
        self.FileName=FileName
        if os.path.isfile(FileName):
            self.Check=1
            
            self.original = cv2.imread(self.FileName)
            self.img=self.ResizeImg(self.original.copy())
            self.GetContours()
            
        else:
            self.Check=0
    def ResizeImg(self,im):
        im=cv2.resize(im,(300,100))
        return im
    def BinaryProcess(self,value=80):
        #x=cv2.resize(self.img,(450,600))
        self.threshold = value
        
        
        bp = ip.Binarization(self.img,self.threshold)
        
        return bp
    def FromUrlSrc(self,im):
        self.img=im
        self.Check=1
        self.GetContours()
    def GetContours(self):
        # Contours = 1 X Length X 1 X Point(x,y)   4 dim
        p= self.BinaryProcess()
        p,contours, heirs = cv2.findContours(p,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        self.contours =contours
        return self.contours
    
    def Draw(self,value=80):
        #x= self.img
        y = self.BinaryProcess(value)
        
        y,contours, heirs = cv2.findContours(y,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        temp=[]
        pic = np.zeros((100,300,3)).astype(np.uint8)
        
        for cnt in contours:
           if cv2.contourArea(cnt)>10:
                
               temp.append(cnt)
               [x,y,w,h] = cv2.boundingRect(cnt)
               cv2.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.drawContours(pic,temp,-1,(255,255,255),2)
        #ip.ShowImg(img)
        return pic,temp
    
class im:
    def __init__(self,ic:ImgClass):
        
        self.original=ic.img.copy()
        img = ic.img.copy()
        self.resize=cv2.resize(img,(800,600))
        bp = ip.Binarization(self.resize,80)
        p,contours, heirs = cv2.findContours(bp,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        pic = np.zeros(self.resize.shape).astype(np.uint8)

        cv2.drawContours(pic,contours,-1,(0,0,255),2)
        ip.CvShow(pic)
if __name__=='__main__':
    ic=ImgClass('5799.jpg')
    i=im(ic)
    
    



