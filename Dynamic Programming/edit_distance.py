# Question: Get the minimum edit distance between two strings

def editDistance(a,b):
    # a = intention
    # b = execution
    cache = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(cache)):
        cache[i][0] = i
    for j in range(len(cache[0])):
        cache[0][j] = j
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                cache[i+1][j+1] = cache[i][j]
            else:
                replace = 1 + cache[i][j]
                delete = 1 + cache[i+1][j]
                insert = 1 + cache[i][j+1]
                cache[i+1][j+1] = min(replace,delete,insert)
    return cache[-1][-1]
