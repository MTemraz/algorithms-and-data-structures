# Question: Given an array of size n, generate and print all possible combinations of k elements in array
#
# Example: 
#   Input: [1,2,3,4], 2
#   Output: [[1, 2],[1, 3],[1, 4],[2, 3],[2, 4],[3, 4]]

def kCombinations(array,k,result=[]):
    if len(result) == k:
        print result
    for i in range(len(array)):
        curr = array[i]
        remaining = array[:i] + array[i+1:]
        kCombinations(remaining,k,result+[curr])

def kCombination2(array, k):
    A = [0]*k
    _kCombination(array, 0, k, 0, A)

def _kCombination2(array, pos, k, start, A):
    if pos == k:
        print A
        return
    for i in range(start,len(array)):
        A[pos] = array[i]
        _kCombination(array, pos+1, k, start+1, A)
    
