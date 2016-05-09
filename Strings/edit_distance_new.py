def editDistance(a,b):
    # a = make
    # b = mike
    DP = [[0]*(len(a)+1) for _ in range(len(b)+1)]
    for i in range(len(a)+1):
        DP[0][i] = i
    for j in range(len(b)+1):
        DP[j][0] = j
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                DP[i+1][j+1] = DP[i][j]
            else:
                insert = DP[i][j+1] + 1
                delete = DP[i+1][j] + 1
                replace = DP[i][j] + 2
                DP[i+1][j+1] = min(insert,replace,delete)
    return DP[-1][-1]

if __name__ == '__main__':
    print(editDistance('intention','execut'))
