import string
from collections import defaultdict

# Write code to transform a source word to a target word given a dictionary of valid words

def createDictionary(words):
    graph = defaultdict(list)
    for word in words:
        deletes = [word[:i]+word[i+1:] for i in xrange(len(word))]
        for d in deletes:
            if d in words:
                graph[word].append(d)
        replaces = [word[:i]+c+word[i+1:] for i in xrange(len(word)) for c in string.lowercase if c!=word[i]]
        for r in replaces:
            if r in words:
                graph[word].append(r)
        adds = [word[:i]+c+word[i:] for i in xrange(len(word)+1) for c in string.lowercase]
        for a in adds:
            if a in words:
                graph[word].append(a)
    return graph

def transform(start,target,graph):
    if start == target:
        return 'same word'
    q = Queue()
    q.enqueue([start])
    while not q.isEmpty():
        currPath = q.dequeue()
        currWord = currPath[-1]
        for w in graph[currWord]:
            if w == target:
                return currPath+[w]
            if w not in currPath:
                q.enqueue(currPath+[w])
    return 'Path not Found'
    

class Queue:
    def __init__(self):
        self.data =[]
    def enqueue(self,v):
        self.data.append(v)
    def dequeue(self):
        return self.data.pop(0)
    def isEmpty(self):
        return len(self.data) == 0
        
if __name__ == '__main__':
    words = ['hot','dot','dog','lot','log','hit','cog']
    graph = createDictionary(words)
    print transform('hit','cog',graph)
