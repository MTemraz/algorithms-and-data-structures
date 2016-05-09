# Question: Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.

def binomial(n,k):
    C = [[0]*(k+1) for _ in range(n+1)] 
    for i in range(n+1):
        #for j in range(min(i,k)+1):
        for j in range(k+1):
            if j > i: continue
            if i==j or j == 0:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[-1][-1]
