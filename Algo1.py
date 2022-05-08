### Lecture 1 ###
### 3 different algorithms for finding peaks in a one-dimensional array ###

def peak1(length, array):
# The first peak finding algorithm looks at each array element sequentially
# and checks if it's equal to or larger than its neighbors
# Input is length of the array and the array (list) itself
# Output is the index of the first peak
# O(n) Time
# O(1) Space
    if array[0] >= array[1]:
        return 0
    for i in range(1,length-2):
        if array[i-1] <= array[i] and array[i] >= array[i+1]:
            return i
    if array[length-2] <= array[length-1]:
        return length-1


def peak2(length, array):
# The second peak finding algorithm searches for a maximum element in the array
# Theoretically and experimentally faster than the first algorithm, since the constants are smaller
# Input is length of the array and the array (list) itself
# Output is the index of the maximum value
# O(n) Time
# O(1) Space
    max = 0
    for i in range(length):
        if array[i] > array[max]:
            max = i
    return max


def peak3(A,i,j):
# The third peak finding algorithm is a recursive divide and conquer algorithm
# Starts at the middle of the array and checks for peak,
# calls itself recursively if no peak is found, further dividing the array
# Input is the array itself, starting index, length of the array
# Output is the index of the maximum value
# O(logn) Time
# O(1) Space
    m = int((i+j)/2)
    if A[m] >= A[m-1] and m >= j:
        return m
    if A[m] >= A[m-1] and A[m] >= A[m+1]:
        return m
    elif A[m-1] > A[m]:
        return peak3(A,i,m-1)
    elif A[m] < A[m+1]:
        return peak3(A,m+1,j)


### input routine for codejudge ###

length = int(input()) # Read line with one input integer
array = list(map(int, input().split())) # Multiple integers on a line

#print(peak1(length, array))
#print(peak2(length, array))
#print(peak3(array,0,length-1))
