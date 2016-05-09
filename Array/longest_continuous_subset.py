# Question: Given an array of integers, return the longest continuous subset.
# Example: 
#    Input: [20,19,21,3,5,4,6,8] 
#    Output: [3,4,5,6]

def longestContinuousSubset(array):
    cache = {num:True for num in array}
    max = 1
    subset_start = array[0]
    for num in array:
        count = 1
        start = num
        left = num - 1
        right = num + 1
        while left in cache:
            count += 1
            start = left
            del cache[left]
            left -= 1
        while right in cache:
            count += 1
            del cache[right]
            right += 1
        if count > max:
            max = count
            subset_start = start
    result = [subset_start]
    for _ in range(max-1):
        subset_start += 1
        result.append(subset_start)
    return result
