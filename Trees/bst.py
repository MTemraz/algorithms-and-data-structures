class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,v):
        if self.root is None:
            self.root = Node(v)
        else:
            _insert(self.root,v)
            
    def delete(self,v):
        if self.root is None:
            return 
        self.root = _delete(self.root,v)

    def contains(self,v):
        if self.root is None:
            return False
        return _contains(self.root,v)
    
    def print_tree(self):
       draw_tree(self.root, 1)

    def traverse(self):
        _traverse(self.root)

def _traverse(root):
    if not root:
        return
    _traverse(root.left)
    print(root.data)
    _traverse(root.right)

def draw_tree(root, depth):
   if root is None:
       return
   draw_tree(root.right, depth + 1)
   print("    " * (depth - 1) + str(root))
   draw_tree(root.left, depth + 1)

def _contains(root,v):
    if not root:
        return False
    if root.data == v:
        return True
    elif v > root.data:
        return _contains(root.right,v)
    else:
        return _contains(root.left,v)

def _delete(root,v):
    if root.data == v:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            pred = find_max(root.left)
            root.data = pred.data
            root.left = _delete(root.left,pred.data)
            return root
    else:
        if v > root.data:
            root.right = _delete(root.right,v)
        else:
            root.left = _delete(root.left,v)
        return root

def find_max(node):
    while node.right:
        node = node.right
    return node

def _insert(root,v):
    if v > root.data:
        if root.right is None:
            root.right = Node(v)
        else:
            _insert(root.right,v)
    else:
        if root.left is None:
            root.left = Node(v)
        else:
            _insert(root.left,v)

counter = 0
def kLargestBST(root,k,L=[]):
    if root is None:
        return 
    kLargestBST(root.right,k)
    global counter
    counter += 1
    if counter == k:
        #return root.data
        L.append(root.data)
    kLargestBST(root.left,k)
    return L

#L = []
def kSmallestBST2(root,k,L=[]):
    if not root:
        return None
    kSmallestBST2(root.left,k,L)
    k -= 1
    if k==0:
        print(root.data)
    kSmallestBST2(root.right,k,L)
    return L

def kSmallest2(root,k):
    stack = []
    stack.append(root)
    counter = 0
    while len(stack) > 0 or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            curr = stack.pop()
            counter += 1
            if counter == k:
                return curr.data
            root = curr.right

def allSumPaths(root, k):
    #path = [root.data]
    #path = ""
    path = []
    result = []
    return dfs(root, k, path, result)

def dfs(root, k, path, result):
    #if not root:
    #    return
    #k -= root.data
    #if k == 0:
    #path += " "+str(root.data)
    if (root.data == k) and (root.left is None) and (root.right is None):
        result.append(path+[root.data])
    #path.append(root.data)
    if root.left:
        dfs(root.left, k-root.data, path+[root.data], result)
    if root.right:
        dfs(root.right, k-root.data, path+[root.data], result)
    return result


def maxPathSum(root):
    max_sum = -1
    max_path = [-1]
    result = [max_sum,max_path]
    _maxPathSum(root,0,[],result)
    return result

def _maxPathSum(root, curr_sum, path, result):
    if not root:
        return
    curr_sum += root.data
    if (not root.left) and (not root.right):        
        if curr_sum > result[0]:
            result[0] = curr_sum
            result[1] = path+[root.data]
    _maxPathSum(root.left, curr_sum, path+[root.data], result)
    _maxPathSum(root.right, curr_sum, path+[root.data], result)

def deepestNode(root, level=0, deepest=[0], node=[None]):
    if not root:
        return
    #level += 1
    if root.left is None and root.right is None:
        if level > deepest[0]:
            deepest[0] = level
            node[0] = root.data
    deepestNode(root.left,level+1,deepest,node)
    deepestNode(root.right,level+1,deepest,node)
    return deepest[0], node[0]

def minDepth(root,curr_level=0,min_depth=[1000],curr_path=[],path=[None]):
    if not root:
        return
    if root.left is None and root.right is None:
        if curr_level < min_depth[0]:
            min_depth[0] = curr_level
            path[0] = curr_path+[root.data]
    minDepth(root.left,curr_level+1,min_depth,curr_path+[root.data],path)
    minDepth(root.right,curr_level+1,min_depth,curr_path+[root.data],path)
    return min_depth[0],path[0]

def maxLeafToLeafSum(root, max_sum):
    if not root:
        return 0
    leftSum = maxLeafToLeafSum(root.left, max_sum)
    rightSum = maxLeafToLeafSum(root.right, max_sum)
    if leftSum == 0 and rightSum == 0:
        curr_sum = root.data
    else:
        curr_sum = max(leftSum+rightSum+root.data, max(leftSum,rightSum))
    print curr_sum
    print max_sum
    if curr_sum > max_sum[0]:
        max_sum[0] = curr_sum
    return max(leftSum,rightSum)+root.data

def maxAnyPathSum(root, max_sum):
    if not root:
        return 0
    leftS = maxAnyPathSum(root.left, max_sum)
    rightS = maxAnyPathSum(root.right, max_sum)
    curr_sum = max(root.data, max(root.data+leftS, root.data+rightS))
    max_sum[0] = max(max_sum[0], max(curr_sum, root.data+leftS+rightS))
    return curr_sum

def identicalTrees(arr1, arr2, arr1_start, arr2_start, minimum, maximum,edge_1=False,edge_2=False):
    if len(arr1) != len(arr2):
        return False
    for i in range(arr1_start, len(arr1)):
        if minimum < arr1[i] < maximum:
            #print arr1[i]
            edge_1 = False
            break
        edge_1 = True
    for j in range(arr2_start, len(arr2)):
        if minimum < arr2[j] < maximum:
            #print arr2[j]
            edge_2 = False
            break
        edge_2 = True
    #if (arr1_start == len(arr1)) and (arr2_start == len(arr2)):
    #    return True
    if (edge_1 or arr1_start == len(arr1)) and (edge_2 or arr2_start == len(arr2)):
        return True
    print arr1[i],arr2[j]
    if arr1[i] == arr2[j]:
        return (identicalTrees(arr1,arr2,i+1,j+1,minimum,arr1[i],edge_1,edge_2)) and (identicalTrees(arr1,arr2,i+1,j+1,arr1[i],maximum,edge_1,edge_2))
    return False

def iterativeInorder(root):
    stack = list()
    #stack.append(root)
    #root = root.left
    result = []
    while len(stack) > 0 or root is not None:
        if root:
            stack.append(root)
            root = root.left
        else:
            curr = stack.pop()
            result.append(curr.data)
            root = curr.right
    return result


def constructTree(preorder):
    idx = 0
    return _constructTree(preorder,idx,-sys.maxint,sys.maxint)

def _constructTree(preorder,idx,low,high):
    if idx[0] >= len(preorder):
	return None
    key = preorder[idx]
    print low,preorder[idx],high
    if low < key and key < high:
	root = Node(key)
	#idx[0] = idx[0] + 1
        idx += 1
        print idx
        root.left = _constructTree(preorder,idx,low,key)
        root.right = _constructTree(preorder,idx,key,high)
        return root
    return None

if __name__ == '__main__':
    import sys
    tree = BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(4)
    tree.insert(3)
    tree.insert(9)
    tree.insert(7)
    tree.insert(8)
    #tree.print_tree()
    #root = tree.root
    #print(iterativeInorder(root))
    preorder = [20,10,5,1,7,15,30,25,35,32,40]
    
    #print(allSumPaths(root,14))
    #max_sum = [-1]
    #maxLeafToLeafSum(root,max_sum)
    #maxAnyPathSum(root, max_sum)
    #print(max_sum)
    #print(deepestNode(root))
    #arr1,arr2 = ([3,5,4,6,1,0,2], [3,1,5,2,4,6,0])
    #arr1, arr2 = ([6,5,9],[6,8,5])
    #print (arr1,arr2)
    #print(identicalTrees(arr1,arr2,0,0,-sys.maxint,sys.maxint))
