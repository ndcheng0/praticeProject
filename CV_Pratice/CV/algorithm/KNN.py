# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 01:13:18 2018
%reset -f

@author: user
"""
import numpy as np
import math
import operator

class KNearst:
    
    trainSet=[]
    response=[]
    
    def GetTrainSet(self):
        #LoadData
        #CreateData
        pass
    def SetTrainSet(self,trainset):
        self.trainSet=trainset
    def euDistance(self,Vector1,Vector2,length):
        dis=0
        
        for i in range(0,length):
            dis+=pow((Vector1[i]-Vector2[i]),2)
        
        return math.sqrt(dis)
            
        
        
    def getNeighbors(self,testset,k=1):
        distances=[]
        length=len(self.trainSet)
        for i in range(0,length-1):
            dist=self.euDistance(self.trainSet[i],testset)
            distances.append((self.trainSet[i],dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors=[]
        for i in range(0,k):
            neighbors.append(distances[i][0])
        return neighbors
    
if __name__=='__main__':
    dic={'a':[1,1]}
    if 'b' in dic:
        print('b')
    else:
        print('abc')
    knn=KNearst()
    a=[2,2,2,'a']
    
    knn.SetTrainSet(a)
    b=[4,4,4,'b']
    dis= knn.euDistance(a,b,3)
    
    
    


