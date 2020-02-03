##def BubbleSort(A):
##    for i in range(len(A)-1):
##        for j in range(len(A)-1-i):
##            if(A[j]>A[j+1]):
##                c = A[j]
##                A[j],A[j+1] = A[j+1],c
##    return A
##p = [100,2,5]
##
##X = BubbleSort(p)
##print(X)


##def CountingSort( aList):
##    c = [0] * ( max(aList) + 1 )
##    for i in aList:
##      c[i] += 1
## 
##    x = 0;
##    for i in range(len(c)):
##      while 0 < c[i]:
##        aList[x] = i
##        x += 1
##        c[i] -= 1
##    return aList
##S = [4,3,8]
##Q = CountingSort(S)
##print(Q)


##def SelectionSort(A):
##    for i in range(len(A)):
##        B = i
##        for j in range((i+1),len(A)):
##            if A[j] < A[B]:
##                B = j
##
##        temp = A[i]
##        A[i],A[B] = A[B],temp
##    return A
##
##S = [4,6,9,8,2]
##Q = SelectionSort(S)
##print(Q)


def InsertionSort(A):
    for i in range(0,len(A)):
        k = A[i]
        j = i-1
        while(j>=0 and A[j]>k):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = k
    return A

S = [4,6,9,8,2]
Q = InsertionSort(S)
print(Q)
