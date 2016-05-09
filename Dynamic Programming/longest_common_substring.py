# Question: Get the length of the longest common substring between 2 strings, also return the substring

def longestCommonSubstring(a,b):
    cache = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    max_result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                cache[i+1][j+1] = cache[i][j]+1
                if cache[i+1][j+1] > max_result:
                    max_result = cache[i+1][j+1]
                    max_index = (i,j)
    longest_substring = []
    a_index,b_index = max_index
    while a[a_index] == b[b_index]:
        longest_substring.append(a[a_index])
        a_index -= 1
        b_index -= 1
    return max_result,''.join(reversed(longest_substring))
