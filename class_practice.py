listofN=[7,5,4,1,9,0,3,-2,21,-6,13]
sortedList=sorted(listofN)

print(listofN)

print(sortedList)

print(listofN==sortedList)

def bubbleSort(list1):

    for i in range(len(list1)-1):

        for i in range(len(list1)-1):
            first=list1[i]
            second=list1[i+1]

            if first>second:
                swap=first
                list1[i]=second
                list1[i+1]=swap

    return list1
