# Question: Given a sorted array, write code to create a bst with min height.

def minHeightTree(array):
    return _minHeightTree(array,0,len(array)-1)

def _minHeightTree(array,start,end):
    if start > end:
        return
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = _minHeightTree(array,start,mid-1)
    node.right = _minHeightTree(array,mid+1,end)
    return node
