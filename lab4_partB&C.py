import time
    
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    x=0
    y=1
    for i in range(n):
        x=x
        y=y+x
        x=y-x
        
    return y

y=500
k=[1,1]
for i in range(y):
    k.append(0)

def fib_dynamic(x):
    if k[x]==0:
        k[x]=fib_dynamic(x-1)+fib_dynamic(x-2)

    return k[x]
        
        

    
def timer(x):

    t1=time.clock()
    fib_dynamic(x)
    print(time.clock()-t1," - time of dynamic")


    t2=time.clock()
    fib(x)
    print(time.clock()-t2, " - time of recursive")

    t3=time.clock()
    fibonacci(x)
    print(time.clock()-t3," - time of linearly")

    
        
    
    
    

         
    
        
        
