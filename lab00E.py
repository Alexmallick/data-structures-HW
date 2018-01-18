n=1
for i in range(2,50):
    isprime= True
    for j in range(2,i):
        if i %j==0:
            isprime= False
    if isprime==True:
        print(i)
