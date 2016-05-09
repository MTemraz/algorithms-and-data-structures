# Question: Get the maximum sum of non-adjacent elements in an array
# Example:
#   Input: [1,2,1,3,1]
#   Output: 5

def maxNonAdjacentSum(array):
    cache = [0] * len(array)
    cache[0] = array[0]
    cache[1] = max(array[0], array[1])
    for i in range(2,len(array)):
        cache[i] = max(cache[i-1], cache[i-2]+array[i])
    return cache[-1]
