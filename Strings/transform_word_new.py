import string
from collections import defaultdict

def createGraph(words):
    graph = defaultdict(list)
    letters = string.lowercase
    for word in words:
        # adds
        graph[word] += [word[:i]+letter+word[i:] for i in range(len(word)+1) for letter in letters
                        if word[:i]+letter+word[i:] in words]
        # deletes
        graph[word] += [word[:i]+word[i+1:] for i in range(len(word)) if word[:i]+word[i+1:] in words]
        
        # replaces
        graph[word] += [word[:i]+letter+word[i+1:] for i in range(len(word)) for letter in letters
                        if word[:i]+letter+word[i+1:] in words and word[:i]+letter+word[i+1:] != word]
    return graph

def transform(start,target,graph):
    path = [[start]]
    while len(path) > 0:
        currPath = path.pop(0)
        currWord = currPath[-1]
        for w in graph[currWord]:
            if w == target:
                return currPath+[w]
            elif w not in currPath:
                path.append(currPath+[w])
                #print currPath+[w]
    return None

    
if __name__ == '__main__':
    graph = createGraph(['hot','dot','dog','lot','log','hit','cog'])
    print(transform('hit','cog',graph))
