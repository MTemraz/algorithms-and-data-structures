
def longestUnique(string):
    # string = 'mmmmmjklomk'
    start = 0
    string_start = 0
    string_end = 0
    currLen = 1
    maxLen = 1
    cache = {string[0]:0}
    for i in range(1,len(string)):
        if string[i] in cache:
            start = cache[string[i]]+1
        else:
            currLen = i-start+1
            if currLen > maxLen:
                maxLen = currLen
                string_start = start
                string_end = i
        cache[string[i]] = i
    return maxLen,string[string_start:string_end+1]

if __name__ == '__main__':
    print(longestUnique('mmmmjklomk'))
