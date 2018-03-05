import wordlist
import time


def word_finder(x):
    i=-1

    while True:
        i=i+1
        list1=wordlist.words
        y=list1[i]
        if y==x:
            print(i)
            break

list1=wordlist.words

##z=0

# to begin the program we take a=0, z=length of list1 which in this case is 25484.
def word_finder1(x,a,z):
    
    mid=int((a+z)/2)
    
    if list1[mid].lower()==x.lower():
        return mid
    else:
        if list1[mid].lower()<x.lower():
            return word_finder1(x,mid+1,z)
        elif list1[mid].lower()>x.lower():
            return word_finder1(x,a,mid-1)

    
    
def timer(x):

    t1=time.clock()
    word_finder(x)
    print(time.clock()-t1," - time of linear search")


    t2=time.clock()
    word_finder1(x,0,25484)
    print(time.clock()-t2, " - time of recursive search")
