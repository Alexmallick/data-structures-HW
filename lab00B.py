op=open("file1.txt","r")
for i in range(1000):
    sen=op.readline()
    if len(sen.split())>=1:
        print (i,sen,end=" ")

