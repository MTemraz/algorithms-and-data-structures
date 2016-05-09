import sys
def isPalin(string):
    n = len(string)
    cache = [[0]*n for _ in range(n)]
    for i in range(n):
        cache[i][i] = True
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if l == 2:
                cache[i][j] = (string[i] == string[j])
            else:
                cache[i][j] = (string[i] == string[j]) and cache[i+1][j-1]
    cuts = [sys.maxint]*n
    for i in range(n):
        if cache[0][i]:
            cuts[i] = 0
        else:
            for j in range(i):
                if cache[j+1][i]:
                    cuts[i] = min(cuts[i],1+cuts[j])
    return cuts
