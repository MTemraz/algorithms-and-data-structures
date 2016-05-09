# Question: Given a array of unsorted numbers, check if all the numbers in the array are consecutive numbers.
#
# Example:
#   Input: [21,24,22,26,23,25]
#   Output: True

def isConsecutive(array):
    # cache = [1,1,1,1,1,1]
    max = max(array)
    min = min(array)
    if max-min+1 != len(array):
        return False
    cache = [0 for _ in array]
    for i in range(len(array)):
        if cache[array[i]-min] != 0:
            return False
        cache[array[i]-min] = 1
    return True
    
