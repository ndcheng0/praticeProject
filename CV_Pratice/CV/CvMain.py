# -*- coding: utf-8 -*
import os
import cv2
import ImageProcess as ip
import threading
import matplotlib.pyplot as plt
from importlib import reload
from MyClass import ImgClass
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import sys
from Classification import Classification
from Mainsys import Mainsys

class CvMain:
    ### 宣告變數 ###
    CurrentFile =''  
    ic:ImgClass = None
    classfy:Classification=None 
    program:Mainsys=None
    main = Tk()
    Btns=[]
    Lbs=[]
    ###############
    
    
    ### 畫布大小  X x Y
    sizeX=600
    sizeY=400
    ###############
    
    
    ### 設定畫布 ###
    ImgCanva=Canvas(main,width=600,height=400,bg='white')
    ConsoleCanva=Canvas(main,width=200,height=150,bg='black')
    Console = ConsoleCanva.create_text(100,75,fill='white',text='Hello!')
    OptionCanva = Canvas(main,width=200,height=300,bg='white')
    ###############

    someword=StringVar(main)
    someword.set('Options')
    
    url_src=StringVar(main)
    url_src.set('輸入Url')
    
    def __init__(self):
        
        main = self.main
        main.title('Py影像辨識')
        main.minsize(1024,680)
        
        self.Component()
        self.CanvaSetting()
        self.Config()
        self.Packing()
        self.PlaceSet()
        self.Option=OptionMenu(self.OptionCanva,self.someword,'One','Two',command=self.OptionOnChange)
       # self.Option.pack()
        
    def Config(self):
        self.SetConfig(self.button,'command',self.OpenFile)
        self.SetConfig(self.button2,'command',self.MainProgram)

        self.SetConfig(self.button3,'command',self.GetContours)
        self.SetConfig(self.button4,'command',self.ClassificationTrain)
        self.SetConfig(self.button5,'command',self.GetContoursFromClassification)
        self.SetConfig(self.button6,'command',self.TrainMainProgram)
        #self.SetConfig(self.button7,'command',self.Url2ic)
    def SetConsole(self,s='Hello!'):
        self.ConsoleCanva.itemconfig(self.Console,text=s)
        
        self.main.update()
        
        
    def SetConfig(self,x,config,action):
        x[config]=action
    def CanvaSetting(self):
        self.ImgCanva.place(x=240,y=100)
        self.ConsoleCanva.place(x=840,y=100)
        self.OptionCanva.place(x=840,y=300)
        #self.ImgLabel = Label(self.ImgCanva,text='Image',fg='white',bg='black')
        #self.ImgLabel.pack()
        #self.ImgCanva.create_window(100,100,window=self.ImgLabel)
    def Component(self):
        self.Filelabel =self.NewLabel('檔案 :')
        self.CanvaLabel = self.NewLabel(str(self.sizeX)+'X'+str(self.sizeY))
        #self.Entry1=Entry(self.main,textvariable=self.url_src,width=50).pack()
        self.button = self.NewButton('開啟檔案')
        self.button2 = self.NewButton('車牌辨識')
        self.button3=self.NewButton('取得Contours')
        self.button4 = self.NewButton('訓練車牌分類系統')
        self.button5=self.NewButton('車牌分類')
        self.button6=self.NewButton('訓練車牌辨識系統')
        #self.button7=self.NewButton("顯示CV圖片")
    def PlaceSet(self):
        self.button.place(x=0,y=50)
        self.button2.place(x=0,y=100)
        self.button3.place(x=0,y=150)
        self.button4.place(x=100,y=50)
        self.button5.place(x=100,y=100)
        self.button6.place(x=0,y=200)
        #self.button7.place(x=0,y=250)
        
    def Packing(self):
        for item in self.Btns:
            item.pack()
        for item in self.Lbs:
            item.pack()
       
    def NewButton(self,s):
        x = Button(self.main,text=s,relief="raised")
        self.Btns.append(x)
        return x
    def NewLabel(self,s):
        x= Label(self.main,text=s)
        self.Lbs.append(x)
        return x
    def ShowThread(self,x,arg):
        ImgThread=threading.Thread(target=x,args=[arg])
        ImgThread.start()
    def BinaryProcess(self):
        if self.ic:
            
            ip.CvShow(self.CurrentFile,self.ic.BinaryProcess())
    def GetContours(self):
        if self.ic:
            pic,contours=self.ic.Draw()
            ip.CvShow(self.CurrentFile,pic)
    def ClassificationTrain(self):
        
        if self.ic :
            #x= os.path.basename(self.CurrentFile) 
            #self.ic=ImgClass(x)
            self.classfy.Trainning()
    def GetContoursFromClassification(self):
        
        if self.ic:
            #x= os.path.basename(self.CurrentFile) 
            #self.ic=ImgClass(x)
            self.classfy.Predict(self.ic,1)
    def TrainMainProgram(self):
        if self.ic and self.program:
            
            self.program.Trainning(self.classfy)

    def MainProgram(self):
        if self.ic and self.program:
            #x= os.path.basename(self.CurrentFile) 
            #self.ic=ImgClass(x)
            pic,contours = self.classfy.Predict(self.ic)
            self.program.Predict(self.ic,contours)
    def Url2ic(self):
        if self.url_src.get():
            url = self.url_src.get()
            cap = cv2.VideoCapture(url)
            if(cap.isOpened()):
                ret,img=cap.read()
                if ret :
                    self.ic = ImgClass('')
                    self.ic.FromUrlSrc(img)
                    self.classfy=Classification(self.ic,self)
                    self.program=Mainsys(self.ic,self)
                    ip.CvShow('N',img)
    def OpenFile(self):
        
        self.CurrentFile =filedialog.askopenfilename(initialdir = r'C:\Users\user\Desktop\CV',
                                      title = "Select file",
                                      filetypes = (
                                                 ("jpeg files","*.jpg"),
                                                      ("all files","*.*"))
                                         )
        if self.CurrentFile:                              
            x= os.path.basename(self.CurrentFile)                           
            self.main.after(5,self.Filelabel.config(text='檔案 :'+x))
            self.ic = ImgClass(x)
            im=Image.open(x)
            if(im.size[0]>600):
                im=im.resize((600,im.size[1]))
            if(im.size[1]>450):
                im=im.resize((im.size[0],450))
        
            
            self.sizeX=im.size[0]
            self.sizeY=im.size[1]
            self.CanvaLabel.configure(text=str(self.sizeX)+'X'+str(self.sizeY))
            img=ImageTk.PhotoImage(image=im)
            self.ImgCanva.create_image(0,0,image=img,anchor=NW)
            self.ImgCanva.image=img
            
            self.classfy=Classification(self.ic,self)
            self.program=Mainsys(self.ic,self)
    def OptionOnChange(self,event):
        #self.Option['text']
        self.SetConsole(event)  
    def deBug(self,x):
        
        im=Image.open('0.jpg')
        
        img=ImageTk.PhotoImage(image=im) 
        
        cvim = cv2.imread('5799.jpg')
        ip.CvShow('5799',cvim)
        
        return img
        print(self.CurrentFile)
    def Run(self):
        self.main.mainloop()
def test(x):
    for i in range(0,10):
        x=x+i
        print(x)
    return x
#TestThread=threading.Thread(target=test,args=[Main.Num]) 




if __name__=='__main__':
    Main = CvMain()
    Main.Run()






    
    
