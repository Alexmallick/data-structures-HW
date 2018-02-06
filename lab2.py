import random
import time

time.time()

waitingRoom=[]

triageRoom=[]

patients=["bobby","tom","harold","jenny","bruce",\
          "stephane","george","thomas","bowie","grant",\
          "kimber","lucas","jonah","joey","monica"]

examRoom=[]

def callNurse():
    triageRoom.append(waitingRoom.pop(0))


class patient:
                
    def __init__(self):
        self.name=random.choice(patients)+" "+random.choice(patients)
        self.pos="waiting room"
        self.visitTime =  int(random.randrange(15,20))
        

    def __str__(self):
        return self.name

def simulate():

    minute=1   

    for i in range(20):
        p = patient()
        waitingRoom.append(p)
     
    while True:
       
        if len(waitingRoom) > 0:
            callNurse()
            
        if len(triageRoom)>0:
            if len(examRoom)<6:
                try:
                    examRoom.append(triageRoom.pop(0))
                except IndexError:
                    break
                    
        else:
            print("examRoom is filled or empty")

        for pat in examRoom:
            pat.visitTime -=1
            print(pat.name,pat.visitTime)
            if pat.visitTime ==0:
                examRoom.remove(pat)
        print("minute"+" "+str(minute))
        print(" ")

        minute=minute+1

        if len(waitingRoom)==0 and len(triageRoom)==0 and len(examRoom)==0:
           break
        

       
simulate()
