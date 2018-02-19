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

k=[]
v=[]

def fib_dynamic(n):
    if n in k:
        a=k.index(n)
        return v[a]
    else:
        if n<=1:
            k.append(n)
            a=k.index(n)
            v.append(1)
            return v[a]
        else:
            v.append(fib_dynamic(n-1)+fib_dynamic(n-2))
            k.append(n)
            a=k.index(n)
            return v[a]

        

    
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

    
        
    
    
    

         
    
        
        
