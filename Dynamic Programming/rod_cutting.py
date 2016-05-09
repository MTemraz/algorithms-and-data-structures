# Question: Given a rod of length n inches and a table of prices pi, i=1,2,…,n, write an algorithm to find the maximum revenue obtainable by cutting up the rod and selling the pieces

def rodCutting(array):
    cache = [0]*(len(array)+1)
    for i in range(1,len(cache)):
        for j in range(i):
            cache[i] = max(cache[i], array[j]+cache[i-(j+1)])
    return cache[-1]

