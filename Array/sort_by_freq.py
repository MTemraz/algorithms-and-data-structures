# Question: Sort an array of integers according to the frequency of elements.

from collections import defaultdict

def sortByFreq(array):
    # array = [1,3,3,4,5,5,5,6,2]
    cache = defaultdict(lambda:0)
    for i in array:
        cache[i] += 1
    items = sorted(cache.items(),key=lambda x:x[1])
    result = []
    for item,freq in items:
        result += [item]*freq
    return result
