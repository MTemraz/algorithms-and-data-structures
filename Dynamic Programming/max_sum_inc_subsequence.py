# Question: Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the intgers in the subsequence are sorted in increasing order.

# Example:
#    Input: [1, 101, 2, 3, 100, 4, 5]
#    Output: 106, formed by [1 + 2 + 3 + 100]
#
#    Input: [3, 4, 5, 10]
#    Output: 22, formed by [3 + 4 + 5 + 10]
#
#    Input: [10, 5, 4, 3]
#    Output: 10, formed by [10]

def maxSumIncSubsequence(array):
    # array = [1, 101, 2, 3, 100, 4, 5]
    # cache = [1, 102, 3, 6, 106, 10,15]
    cache = [i for i in array]
    for i in range(len(array)):
        for j in range(i):
            if array[i] > array[j] and cache[i] < cache[j]+array[i]:
                cache[i] = cache[j]+array[i]
    max_value = max(cache)
    max_index = cache.index(max_value)
    curr_value = max_value
    result = []
    for i in reversed(range(len(cache))):
        if cache[i] == curr_value:
            result.append(array[i])
            curr_value -= array[i]
    return max_value, list(reversed(result))
