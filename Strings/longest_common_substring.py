
def lcs(X,Y):
    DP = [[0]*(len(X)+1) for i in xrange(len(Y)+1)]
    result = ''
    for i in xrange(len(Y)):
        for j in xrange(len(X)):
            if Y[i] == X[j]:
                print X[j]
                DP[i+1][j+1] = DP[i][j] + 1
            else:
                DP[i+1][j+1] = max(DP[i+1][j],DP[i][j+1])
    return DP[-1][-1],DP


if __name__ == '__main__':
    print(lcs('abcdef','acbdee'))
