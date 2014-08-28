# Write code to find the minimum edit distance between 2 strings

def minEditDist(a,b,levenshtein=False):
    if len(a)<len(b):
        a += '$'*(len(b)-len(a))
    elif len(b)<len(a):
        b += '$'*(len(a)-len(b))
    if not a:
        return len(b)
    elif not b:
        return len(a)
    m = len(a)+1
    n  =len(b)+1
    DP = [[0]*m for _ in xrange(n)]
    for i in xrange(m):
        DP[0][i] = i
    for j in xrange(n):
        DP[j][0] = j
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            if a[i] == b[j]:
                DP[i+1][j+1] = DP[i][j]
            else:
                replace = DP[i][j] + 2
                delete = DP[i+1][j] + 1
                insert = DP[i][j+1] + 1
                DP[i+1][j+1] = min(replace,delete,insert)
    return DP[-1][-1]

if __name__ == '__main__':
    print minEditDist('intention','execution')
