### Lecture 2 ###
### Sesrching & Sorting algorithms ###

#from sqlalchemy import true

array = [1,3,5,7,9]
num = 10
unsorted = [3,9,7,1,5]

def BinarySearch(A,i,j,x):
    if j < i:
        return False
    m = int((i+j)/2)
    if A[m] == x:
        return True
    elif A[m] < x:
        return BinarySearch(A,m+1,j,x)
    else:
        return BinarySearch(A,i,m-1,x) # A[m] > x


def InsertionSort(A,n):
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
    return A


def MergeSort(A,i,j):
    if i < j:
        m = int((i+j)/2)
        MergeSort(A,i,m)
        MergeSort(A,m+1,j)
        Merge(A,i,m,j)

def Merge(a,i,m,j):
    return i+m


print(InsertionSort(unsorted,len(unsorted)))
#print(BinarySearch(array,0,4,num))

### input routine for codejudge ###

#length = int(input()) # Read line with one input integer
#array = list(map(int, input().split())) # Multiple integers on a line

#print(peak1(length, array))
#print(peak2(length, array))
#print(peak3(array,0,length-1))

