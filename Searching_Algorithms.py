##def LinearSearch(A,key):
##    c = 0
##    for i in range(len(A)):
##        if(A[i] == key):
##            c = 1
##            index = i
##            break
##        else:
##            continue
##
##    if(c == 1):
##        print("Data Found at index",index)
##    else:
##        print("Data Not Found")
##
##B = [10,20,12,48,87]
##LinearSearch(B,12)

def BubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if(A[j]>A[j+1]):
                d = A[j]
                A[j],A[j+1] = A[j+1],d
    return A

def BinarySearch(A,key):
    B = BubbleSort(A)
    c = 0
    f = 0
    l = len(B)-1

    for i in range(len(B)):
        m = (f+l)//2
        if(B[m] == key):
            c = 1
            break
        elif(B[m] < key):
            f = m+1
        elif(B[m] > key):
            l = m-1
    if(c == 1):
         print("Data Found")
    else:
         print("Data Not Found")

B = [10,20,12,48,87]
BinarySearch(B,12)


        
