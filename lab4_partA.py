import time
#this function gives the number of steps required for a number to reach "1" if divided by 2.
def collatz(n):
    if n<=2:
        return 1
    elif n%2==0:
        return 1+collatz(n/2)
    elif n%2!=0:
        return 2+collatz((3*n+1)/2)


        
