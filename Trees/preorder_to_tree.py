import sys

def constructTree(preorder):
    idx = [0]
    return _constructTree(preorder,idx,-sys.maxint,sys.maxint)

def _constructTree(preorder,idx,low,high):
    if idx[0] >= len(preorder):
        return None
    key = preorder[idx[0]]
    #print low,preorder[idx[0]],high
    if low < key and key < high:
        root = Node(key)
        idx[0] = idx[0] + 1
        #print idx
        root.left = _constructTree(preorder,idx,low,key)
        root.right = _constructTree(preorder,idx,key,high)
        return root
