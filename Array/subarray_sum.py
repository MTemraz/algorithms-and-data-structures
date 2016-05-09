# Quesion: Given an array and an integer, find the continuous subarray whose sum is equal to the given integer.
#
# Example:
#   Input: [25, 12, 14, 22, 19, 15, 10, 23], 55
#   Output: [14,22,19]

def subarraySum(array, k):
    # array = [25, 12, 14, 22, 19, 15, 10, 23]
    curr_sum = 0
    start = 0
    for i in range(len(array)):
        curr_sum += array[i]
        while curr_sum > k:
            curr_sum -= array[start]
            start += 1
        if curr_sum == k:
            return array[start:i+1]
        
