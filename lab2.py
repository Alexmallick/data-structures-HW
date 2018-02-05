import random
import time

import re

#this function was used from the stack overflow to do the sorting.
_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]

time.time()

waitingRoom=[]

triageRoom=[]

patients=["bobby","tom","harold","jenny","bruce",\
          "stephane","george","thomas","bowie","grant",\
          "kimber","lucas","jonah","joey","monica"]

examRoom=[]

def callNurse():
    triageRoom.append(waitingRoom.pop(0))
    triageRoom.sort(key=natural_sort_key)



class patient:
                
    def __init__(self):
        self.triageNumber=random.randrange(1,10)
        self.name=str(self.triageNumber)+" "+random.choice(patients)+" "+random.choice(patients)
        self.pos="waiting room"
        self.visitTime=random.randrange(15,20)
        waitingRoom.append(self.name)
        self.time1=int(time.clock())


    def erEntry(self):
        self.time1=self.time1+120
        if len(examRoom)<6:
            examRoom.append(triageRoom.pop(0))
        else:
            print("examRoom is filled")

    def rem(self):
        while True:
            if time.clock()==self.time1+self.visitTime:
                examRoom.remove(self.name)
                break



