# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import ImageProcess as ip
import cv2
class Bug:
    url='https://www.google.com.tw/search?q=%E8%BB%8A%E7%89%8C%E8%99%9F%E7%A2%BC&newwindow=1&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjArbGZ3aPeAhWFwrwKHaHpAUkQ_AUIDigB&biw=1366&bih=695'

    
    def __init__(self):
        r= requests.get(self.url)
        self.r=r
        if r.status_code == requests.codes.ok:
            # 以 BeautifulSoup 解析 HTML 程式碼
          soup = BeautifulSoup(r.text, 'html.parser')
          # 以 CSS 的 class 抓出各類
          #print(soup)
          imgs = soup.find_all('img')
          print(len(imgs))
          for img in imgs:
              c = img.get('alt')
              print(c)
              urlsrc=img.get('src')
              print(urlsrc)
              cap = cv2.VideoCapture(urlsrc)
              if(cap.isOpened()):
                ret,img=cap.read()
                if ret :
                    
                    ip.CvShow('N',img)
          
          
        else:
            print('Wrong Request')



    
    
if __name__=='__main__':
    b = Bug()
   