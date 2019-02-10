import numpy as np
import os
import cv2
import ImageProcess as ip
import sys
import matplotlib.pyplot as plt
from importlib import reload
from MyClass import ImgClass
from Classification import Classification
from DataBase import Code

class Mainsys:
    def __init__(self,ic:ImgClass ,Main):
        
        self.Code = Code()
        self.ic =ic
        self.Main=Main
       
        
    def LoadData(self):     
        
        self.samples = np.loadtxt('samples.data',np.float32)
        self.responses = np.loadtxt('res.data',np.float32)
        self.responses = self.responses.reshape((self.responses.size,1))
    def CreateKNN(self):
        
        self.model = cv2.ml.KNearest_create()
        self.model.train(self.samples,cv2.ml.ROW_SAMPLE,self.responses)
    def Trainning(self,Classify:Classification): 
        
        Main=self.Main
        Main.SetConsole('Train!')
        Target = self.ic
        pic,ClassContours =  Classify.Predict(Target)
        process = Target.BinaryProcess()
        
        #area = ip.MappingCnt(contours)
        if os.path.isfile('samples.data') and os.path.isfile('res.data'):
            print('LoadData')
            Main.SetConsole('LoadData!')
            samples = np.loadtxt('samples.data',np.float32)
            responses = np.loadtxt('res.data',np.float32)
            
        else:
            print ('NewData')
            Main.SetConsole('NewData!')
            samples =  np.empty((0,100))
            responses = []
        
        keys = [i for i in range(48,58)] + [j for j in range(97,123)]
        close = 0
        for cnt in ClassContours :
            original=Target.img.copy()
            [x,y,w,h] = cv2.boundingRect(cnt)
            cv2.rectangle(original,(x,y),(x+w,y+h),(0,0,255),2)
            TargetPxs=process[y:y+h,x:x+w]
            TargetPxsSmall=cv2.resize(TargetPxs,(10,10))
           
            cv2.imshow('CarLicense',original)
            while close==0:
                key = cv2.waitKey(100)
                if key!=-1:
                    print(key)
                if cv2.getWindowProperty('CarLicense',0)==-1:
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
                    
                    
                
                elif key in keys:
                    responses=np.append(responses,key)
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
        
        np.savetxt('samples.data',samples)
        np.savetxt('res.data',responses)
        return 1
    
         
        
        
        
        
    def Predict(self,ic:ImgClass,contours):
        
        self.LoadData()
        self.CreateKNN()
        
        Target = ic
        original = Target.img.copy()
        process = Target.BinaryProcess()
        out = np.zeros(Target.img.shape,np.uint8)
        
        for cnt in contours:
            if cv2.contourArea(cnt)>50:
                [x,y,w,h] = cv2.boundingRect(cnt)
                
                
                cv2.rectangle(original,(x,y),(x+w,y+h),(0,0,255),2)
                TargetPxs=process[y:y+h,x:x+w]
                TargetPxsSmall=cv2.resize(TargetPxs,(10,10))
                sample = TargetPxsSmall.reshape((1,100))
                sample=np.float32(sample)
                retval, results, neigh_resp, dists = self.model.findNearest(sample, k = 1)
                
                string = self.Code.deCode(results[0][0])
                cv2.putText(out,string,(x,y+h),0,1,(0,255,0))
               
                
        
        ip.CvShow('Out',out)


