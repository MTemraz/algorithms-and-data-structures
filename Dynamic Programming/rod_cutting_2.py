def rodCutting(array):
    cache = [0]*(len(array)+1)
    for j in range(len(array)):
        print array[j]
        for i in range(1,len(cache)):
            if i >= j+1:
                cache[i] = max(cache[i], array[j]+cache[i-(j+1)])
        print cache
    return cache
