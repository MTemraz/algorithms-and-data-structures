def cS(L):
    temp_array = [0]*(max(L)+1)
    final_array = [0]*len(L)
    for i in range(len(L)):
        temp_array[L[i]] += 1
    for i in range(1,len(temp_array)):
        temp_array[i] += temp_array[i-1]
    for i in reversed(range(len(L))):
        final_array[temp_array[L[i]]-1] = L[i]
        temp_array[L[i]] -= 1
    return final_array
