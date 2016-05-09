# Question: Given a array A[1..n], calculate B[1..m] with B[i]<B[i+1] where i=1,2,3,.…,m such that m is maximum.

def longestIncSubsequence(array):
    # array = [1,12,7,0,23,11,52,31,61,69,70,2]
    cache = [1]*len(array)
    for i in range(len(array)):
        for j in range(i):
            if array[i]>array[j]:
                cache[i] = max(cache[i], cache[j]+1)
    max_sequence = max(cache)
    max_index = cache.index(max_sequence)
    curr_sequence = max_sequence
    result = []
    for i in reversed(range(len(cache))):
        if cache[i] == curr_sequence:
            result.append(array[i])
            curr_sequence -= 1
    return max_sequence, list(reversed(result))

# Follow-up: Return the subsequence
