class listItem:

    def __init__(self,value,index):
        self.value = value
        self.index = index
        self.next = None
        self.previous = None

##class stackItem:
##
##    def __init__(self,value,index):
##        self.value = value
##        self.index = index
##        self.next = None       
##
class myList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self,value):
        li=listItem(value,self.length)
        
        if self.length==0:
            self.head = li
        else:
            li.previous = self.tail
            self.tail.next = li

        self.tail=li
            
        self.length += 1


    def remove(self):

        if self.length ==0:
            pass
        else:
            self.head = self.head.next
            self.length = self.length - 1 

    def __str__(self):
        output=str(self.head.value)

        ci = self.head
        for i in range(self.length - 1):
            ci = ci.next
            output +=(", "+str(ci.value))

        return output



class stackList:

    def __init__(self):
        self.top=None
        self.length=0

    def add(self,value):
        ni=listItem(value,self.length)

        if self.length==0:
            self.top=ni
        else:
            ni.next=self.top

        self.top=ni

        self.length += 1


    def remove(self):

        if self.length ==0:
            pass
        else:
            self.top = self.top.next
            self.length = self.length - 1

    def __str__(self):
        
        output=str(self.top.value)

        ci1 = self.top
        
        for i in range(self.length - 1):
            ci1 = ci1.next
            output +=(", "+str(ci1.value))
            
            
        return output
        
        


newlist=myList()
newlist.add(7)
newlist.add(3)
newlist.add(14)
newlist.add(1)
newlist.add(21)
newlist.add(0)
newlist.add(0)
newlist.add(56)
print(newlist)
newlist.remove()
print(newlist)

list1=stackList()
list1.add(7)
list1.add(3)
list1.add(14)
list1.add(1)
list1.add(21)
list1.add(0)
list1.add(0)
list1.add(56)

print(list1)
list1.remove()

print(list1)
