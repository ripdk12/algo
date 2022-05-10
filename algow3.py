n = int(input())
#arr = list(map(int, input().split()))
arr = [int(i) for i in input().split()]

#print(n)
#print(arr)

def maxSubArray(array, size):

    max_so_far =array[0]
    curr_max = array[0]
     
    for i in range(1,size):
        curr_max = max(array[i], curr_max + array[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far

print(maxSubArray(arr, n))