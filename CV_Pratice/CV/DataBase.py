# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 03:06:35 2018
%reset -f
@author: user
"""

import cv2
import sys
import numpy as np
import os
import struct

class Code:
    KeyCode={
            48:'0',
            49:'1',
            50:'2',
            51:'3',
            52:'4',
            53:'5',
            54:'6',
            55:'7',
            56:'8',
            57:'9',
            97:'A',
            98:'B',
            99:'C',
            100:'D',
            101:'E',
            102:'F',
            103:'G',
            104:'H',
            105:'I',
            106:'J',
            107:'K',
            108:'L',
            109:'M',
            110:'N',
            111:'O',
            112:'P',
            113:'Q',
            114:'R',
            115:'S',
            116:'T',
            117:'U',
            118:'V',
            119:'W',
            120:'X',
            121:'Y',
            122:'Z'
            }
   
    
    #def __init__(self):
        # Do somthing
    def deCode(self,Num:int):
        return   self.KeyCode[Num]      

def Debug():
    pic = np.zeros((450,600,3)).astype(np.uint8)
    cv2.namedWindow('Name',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Name',pic)
    while True:
        key = cv2.waitKey(100)
        if key!=-1:
            print(key)
        if key == 27:  # (escape to quit)
            #sys.exit()        
            print('Esc')
            break
    cv2.destroyAllWindows()
class FileData:
    ClassfyLength:int
    ProgramLength:int
    ClassfyName=[]
    ProgramName=[]
    fn = 'FileData.data'
                   
class data:
    """
    Format	C Type	Python	字节数
    x	pad byte	no value	1
    c	char	string of length 1	1
    b	signed char	integer	1
    B	unsigned char	integer	1
    ?	_Bool	bool	1
    h	short	integer	2
    H	unsigned short	integer	2
    i	int	integer	4
    I	unsigned int	integer or long	4
    l	long	integer	4
    L	unsigned long	long	4
    q	long long	long	8
    Q	unsigned long long	long	8
    f	float	float	4
    d	double	float	8
    s	char[]	string	1
    p	char[]	string	1
    P	void *	long
    """
    id:int
    name:str
    value:float
    
    
def Debug():
    d = data()
    d.id=123
    d.name='abcde'
    d.value=5.4
    sys.getsizeof(d.name.encode('utf8'))
    sys.getsizeof(''.encode('utf8'))
    attrs=vars(d)
    len(d.name)
    with open('test.d','wb') as f:
        f.write(struct.pack('i5sd',d.id,d.name.encode('utf8'),d.value))
    
    newD = data()   
    with open('test.d','rb') as f:
    
        os.path.getsize('test.d')
        byte=f.read(4)
        
        newD.id=struct.unpack('i',byte)
        b= f.read(5)
        newD.name=struct.unpack('5s',b)
        g=f.read(7)
        c=f.read(8)
        newD.value=struct.unpack('d',c)
        print(newD.id,newD.name,newD.value)

    
        
        
        
        