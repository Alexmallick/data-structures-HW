import wordlist


def word_finder(x):
    i=-1

    while True:
        i=i+1
        list1=wordlist.words
        y=list1[i]
        if y==x:
            print(i)
            break

##list1=wordlist.words
##n=len(list1)-1
##y=n
##z=0
##
##def word_finder1(x):
##    global n
##    global y
##    global z
##    if list1[n].lower()==x.lower():
##        return n
##    else:
##        if list1[round(n/2)].lower()<x.lower():
##            y=n/2
##            
##            n=round(n/4)
##        elif list1[round(n/2)].lower()>x.lower():
##            n=round(((n/2)+y)/2)
##            y=
##            
##        print(n)
##        return word_finder1(x)
##    
##    
 
