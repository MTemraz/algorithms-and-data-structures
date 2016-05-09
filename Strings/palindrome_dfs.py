# Question: Given a string s, partition s such that every substring of the partition is a palindrome.

def allPalinSubstrings(string):
    result  = []
    cache = [[False]*len(string) for _ in range(len(string))]
    #for i in range(len(string)):
    #    cache[i][i] = True
    for l in range(1,len(string)+1):
        for i in range(len(string)-l+1):
            j = i+l-1
            if l <= 2:
                cache[i][j] = (string[i] == string[j])
            else:
                cache[i][j] = (string[i] == string[j]) and (cache[i+1][j-1])
    return cache

def dfs(string, cache, start, path=[], result = []):
    if start == len(string):
        result.append(path)
    for i in range(start+1,len(string)+1):
        if cache[start][i-1]:
            dfs(string,cache,i,path+[string[start:i]],result)
    return result

if __name__ == '__main__':
    print(allPalinSubstrings('aabaa'))
