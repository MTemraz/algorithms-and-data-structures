# Question: Given an array of integers and a number k, return True if there is a subset that sums to k

def subsetSum(array, k):
    S = [[False]*(k+1) for _ in range(len(array)+1)]
    for i in range(len(array)+1):
        S[i][0] = True
    for j in range(1,k+1):
        for i in range(1,len(array)+1):
            if j >= array[i-1]:
                S[i][j] = S[i-1][j] or S[i-1][j-array[i-1]]
            else:
                S[i][j] = S[i-1][j]
    return S[-1][-1]
