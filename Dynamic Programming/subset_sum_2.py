# Question: Follow-up on subset_sum.py, return the subset.

def subsetSum(array, k):
    cache = [[False]*(k+1) for _ in range(len(array)+1)]
    for i in range(len(cache)):
        cache[i][0] = True
    for i in range(1,len(array)+1):
        for j in range(1,k+1):
            if j >= array[i-1]:
                cache[i][j] = cache[i-1][j] or cache[i-1][j-array[i-1]]
            else:
                cache[i][j] = cache[i-1][j]
    if not cache[-1][-1]:
        return False
    else:
        row = len(array)
        column = k
        result = []
        while column > 0:
            if cache[row-1][column]:
                row -= 1
            else:
                row -= 1
                column -= array[row]
                result.append(array[row])
        return result
