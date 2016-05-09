def wordBreak2(string, dictionary):
    cache = [list() for i in range(len(string)+1)]
    for i in range(1,len(string)):
        prefix = string[:i]
        if prefix in dictionary:
            cache[i].append(prefix)
        if len(cache[i]) != 0:
            for j in range(i,len(string)+1):
                suffix = string[i:j]
                if suffix in dictionary:
                    cache[j].append(suffix)
                #if j == len(string)-1 and cache[j] != 0:
                #    return True
    return cache

def dfs(cache,index,path=[]):
    if index == 0:
        print ' '.join(reversed(path))
    for word in cache[index]:
        new_index = index - len(word)
        path += [word]
        dfs(cache, new_index, path)
        path.pop()

if __name__ == '__main__':
    dictionary = {"cat", "cats", "and", "sand", "dog"}
    string = 'catsanddog'
    cache = wordBreak2(string,dictionary)
    print cache
    dfs(cache,len(cache)-1)
