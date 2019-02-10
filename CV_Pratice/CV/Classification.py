import numpy as np
import os
import cv2
import ImageProcess as ip
import sys
import matplotlib.pyplot as plt
from importlib import reload
from MyClass import ImgClass


class Classification:
    def __init__(self,ic,Main):
        self.LoadData()
        self.CreateKNN()
        self.ic =ic
        self.Main=Main
    def LoadData(self):     
        
        self.samples = np.loadtxt('CarLicenseSample.data',np.float32)
        self.responses = np.loadtxt('CarLicenseRes.data',np.float32)
        self.responses = self.responses.reshape((self.responses.size,1))
    def CreateKNN(self):
        
        self.model = cv2.ml.KNearest_create()
        self.model.train(self.samples,cv2.ml.ROW_SAMPLE,self.responses)
    def Trainning(self):
        Main=self.Main
        Main.SetConsole('Train!')
        Target = self.ic
        original = Target.img.copy()
        process = Target.BinaryProcess()
        final,contours = Target.Draw()
        #area = ip.MappingCnt(contours)
        if os.path.isfile('CarLicenseSample.data') and os.path.isfile('CarLicenseRes.data'):
                print('LoadData')
                Main.SetConsole('LoadData!')
                samples = np.loadtxt('CarLicenseSample.data',np.float32)
                responses = np.loadtxt('CarLicenseRes.data',np.float32)
                
        else:
            print ('NewData')
            Main.SetConsole('NewData!')
            samples =  np.empty((0,100))
            responses = []
        keys = [i for i in range(48,50)]
        close = 0
        for cnt in contours :
            original=Target.img.copy()
            [x,y,w,h] = cv2.boundingRect(cnt)
            cv2.rectangle(original,(x,y),(x+w,y+h),(0,0,255),2)
            TargetPxs=process[y:y+h,x:x+w]
            TargetPxsSmall=cv2.resize(TargetPxs,(10,10))
           
            cv2.imshow('norm',original)
            while close==0:
                key = cv2.waitKey(100)
                if key!=-1:
                    print(key)
                if cv2.getWindowProperty('norm',0)==-1:
                    print('Close')
                    Main.SetConsole('Close!')
                    close=1
                    
                if key == 27:  # (escape to quit)
                    cv2.destroyAllWindows()
                    close =1
                    print('Esc')
                    Main.SetConsole('Esc!')
                    
                elif key== 32:
                    print('Skip')
                    Main.SetConsole('Skip!')
                    
                    
                elif key==ord('s'):
                    ip.CvShow('ic.img',Target.img)
                    Main.SetConsole('Show!')
                elif key in keys:
                    responses=np.append(responses,int(chr(key)))
                    sample = TargetPxsSmall.reshape((1,100))
                    samples = np.append(samples,sample,0)
                    Main.SetConsole('Add Sample!')
                    break
                
            if close==1:
                return 0
            
        cv2.destroyAllWindows()
        responses = np.array(responses,np.float32)
        responses = responses.reshape((responses.size,1))
        print ('training complete')
        Main.SetConsole('訓練完成，進行存檔!')
        cv2.destroyAllWindows()
        np.savetxt('CarLicenseSample.data',samples)
        np.savetxt('CarLicenseRes.data',responses)
        return 1
    def Predict(self,ic,option=0):
        self.LoadData()
        self.CreateKNN()
        Target = ic
        original = Target.img.copy()
        process = Target.BinaryProcess()
        final,contours = Target.Draw()
        NewContours=[]
        for cnt in contours :
            [x,y,w,h] = cv2.boundingRect(cnt)
            cv2.rectangle(original,(x,y),(x+w,y+h),(0,0,255),2)
            TargetPxs=process[y:y+h,x:x+w]
            TargetPxsSmall=cv2.resize(TargetPxs,(10,10))
            sample = TargetPxsSmall.reshape((1,100))
            sample=np.float32(sample)
            retval, results, neigh_resp, dists = self.model.findNearest(sample, k = 3)
            if(results==1):
                
                NewContours.append(cnt)
                
        pic = np.zeros((450,600,3)).astype(np.uint8)
        
        cv2.drawContours(pic,NewContours,-1,(255,255,255),2)
        if(option==1):
            ip.CvShow('Classification',pic)
        return pic,NewContours
