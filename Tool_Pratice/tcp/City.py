import numpy as np
import time
import threading as thd
import random

class City():
    hitpoints = 100
    techpoints = 0
    food = 0
    Name = "Default"
    population = 0
    money=0
    timeset=0
    farmer=0

    def __init__(self):

        pass

    def load(self):
        pass

    def save(self):

        pass

    def start(self):
        self.techpoints += 2
        self.food += 20
        self.population += 10
        self.money=10
        self.farmer=1

    def timer(self):
        self.timeset += 1
        thd.Timer(1,self.timer).start()
        #print(self.timeset)
        if self.timeset==2:
            self.timeset=0
            self.main()
    def main(self):
        self.ConsumeFood = self.population/4
        self.food -= self.ConsumeFood
        self.ProduceFood = self.farmer*1.2+self.population*0.05
        self.food += self.ProduceFood
        if self.food < 0:
            self.population -= 1
        if self.food > 20:
            dice = random.random()
            if dice > 0.5:
                dice2 = random.random()
                if dice2 > 0.75:
                    self.food -= 15
                    self.farmer += 1
                else :
                    self.food -= 15
                    self.population += 1
        print("p :"+str(self.population))
        print("f :"+str(self.food))
        print("Farmer :"+str(self.farmer))
    def upgrade(self):
        pass

    def new(self):
        self.start()
        self.timer()
if __name__ == '__main__':
    c = City()
    c.new()
