# Write code to find the longest string unique characters

def longestUnique(string):
    cache = {string[0]:0}
    currLen = 1
    maxLen = 1
    prev = 0
    for i in range(1,len(string)):
        if string[i] not in cache:
            cache[string[i]] = i
            currLen = i - prev+1
            maxLen = max(currLen,maxLen)
        else:
            prev = cache[string[i]]+1
            cache = {}
    return maxLen
