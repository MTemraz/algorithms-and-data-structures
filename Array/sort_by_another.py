# Question: Sort an array by the order it appears in another.

from collections import defaultdict
def sortByAnother(A,B):
    # A = [3,7,1,5,3,5]
    # B = [1,7,3,3,3,4,8] -> [3,7,1,4,8]
    cache = defaultdict(lambda:0)
    result = []
    for element in B:
        cache[element] += 1
    for element in A:
        if element in cache:
            result += [element]*cache[element]
            del cache[element]
    remaining = sorted(cache.items())
    for element,freq in remaining:
        result += [element]*freq
    return result
