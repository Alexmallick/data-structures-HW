import random

class waitingRoom:
    def __init__(self): #here wRoom means patients in waiting room and eRoom means patient in examroom.
        self.wRoom=20

class examRoom:
    def __init__(self):
        self.eRoom=[]
        

class patient:
    def __init__(self,name):
        self.name=name
        self.pos="waiting room"
        self.visitTime=random.randrange(15,20)
        self.triaged=False
        self.totaltime=0
        self.visitedDoctor=False

    def nextStep(self):
        self.totaltime=self.totaltime+1

    def visit(self):
        self.visitedDoctor=True
        
class nurse:
    def __init__(self,name):
        self.name=name
        
    def triagePatient(self,pname):
        pname.triaged=True
        pname.nextStep()
            






        
class physician:
    def __init__(self,name,roomNo):
        self.name=name
        self.roomNo=roomNo

##    def currentPatient(self):
##
##        
