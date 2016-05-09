class Node:

    def __init__(self,letter):
        self.letter = letter
        self.isWord = False
        self.children = {}

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

    def __contains__(self,word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.isWord
        
    def getPrefixes(self,word):
        curr = self.root
        prefixes = []
        prefix = ''
        for letter in word:
            if letter not in curr.children:
                return prefixes
            curr = curr.children[letter]
            prefix += letter
            if curr.isWord:
                curr = self.root
                prefixes.append(prefix)
        return prefixes

    def getWords(self,word):
        ''' gets words made from input word, not necessarily prefixes'''
        curr = self.root
        words = []
        sequence = ''
        for letter in word:
            if letter not in curr.children:
                curr = self.root
                sequence = ''
                continue
            curr = curr.children[letter]
            sequence += letter
            if curr.isWord:
                curr = self.root
                words.append(sequence)
                sequence = ''
        return words
    
if __name__ == '__main__':
    words = ['cat','catie','dog','dogball']
    dictionary = Trie()
    for word in words:
        dictionary.insert(word)
    print dictionary.getPrefixes('catdogdoggie')
    print dictionary.getWords('catdogdoggie')
