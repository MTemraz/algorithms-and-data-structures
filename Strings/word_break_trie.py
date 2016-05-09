# This implementaion solves the famous word break problem in linear time

def segment(text,dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    return trie.getSegmentations(text)

# Below is the implementation of the Trie DataStructure
class Node:

    def __init__(self,letter):
        self.letter = letter
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node('')

    def insert(self,word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node(letter)
            curr = curr.children[letter]
        curr.isWord = True

    def getSegmentations(self,word):
        curr = self.root
        segments = []
        prefix = ''
        unseen = False
        for letter in word:
            if letter not in curr.children:
                if unseen: return False
                curr = self.root
                prefix = ''
                unseen = True
                continue
            curr = curr.children[letter]
            prefix += letter
            if curr.isWord:
                segments.append(prefix)
                prefix = ''
                curr = self.root
        return ' '.join(segments)

if __name__ == '__main__':
    dictionary = ['timmy','name','machine','nlp','bayesian','hierarchical','my','and','is']
    print segment('mynameistimmy',dictionary)
