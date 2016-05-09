# Question: Given an array of strings, write code to output all pairs when concatenated, can form a palindrome.
# Exmaple:
#   Input: ['bat','tab','tic','it','cat','dog','a','ba']
#   Output: [('bat','tab'),('tic','it'),('a','ba')]

from collections import defaultdict
def palindromePair(array):
    cache = defaultdict(lambda:0)
    for word in array:
        cache[word] += 1
    for word in array:
        reverse = ''.join(reversed(word))
        if reverse in cache:
            if len(word) == 1:
                if cache[reverse] > 1:
                    print word,reverse
            else:
                print word,reverse
        for i in range(1,len(reverse)):
            if isPalindrome(reverse[:i]) and reverse[i:] in cache:
                print word, reverse[i:]
            elif reverse[:i] in cache and isPalindrome(reverse[i:]):
                print reverse[:i], word

def isPalindrome(word):
    left = 0
    right = len(word)-1
    while left<right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    palindromePair(['bat','tab','tic','it','cat','dog','a','ba'])