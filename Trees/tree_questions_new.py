from bst import *

def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    diff = abs(leftHeight-rightHeight)
    if diff > 1:
        return False
    return max(leftHeight,rightHeight)+1

def isBalanced(root):
    if getHeight(root):
        return True
    return False

def minHeightTree(array):
    if len(array)<1:
        return
    mid = (len(array)-1) // 2
    root = Node(array[mid])
    root.left = minHeightTree(array[:mid])
    root.right = minHeightTree(array[mid+1:])
    return root

def minHeightTree2(array,start,end):
    if start > end:
        return
    mid = (start+end) // 2
    root = Node(mid)
    root.left = minHeightTree2(array,start,mid-1)
    root.right = minHeightTree2(array,mid+1,end)
    return root

def levelTraversal(root):
    q = Queue()
    q.enqueue(root)
    curr = 1
    nxt = 0
    while not q.isEmpty():
        node = q.dequeue()
        print node.data,
        curr -= 1
        if node.left:
            q.enqueue(node.left)
            nxt += 1
        if node.right:
            q.enqueue(node.right)
            nxt += 1
        if curr == 0:
            print('\n')
            curr,nxt = nxt,curr

def treeToLL(root):
    q = Queue()
    q.enqueue(root)
    curr,nxt = 1,0
    ll = LinkedList()
    while not q.isEmpty():
        node = q.dequeue()
        ll.insert(node)
        curr -= 1
        if node.left:
            q.enqueue(node.left)
            nxt += 1
        if node.right:
            q.enqueue(node.right)
            nxt += 1
        if curr == 0:
            ll = LinkedList()
            curr,nxt = nxt,curr

def isBST(root,L=[]):
    if not root:
        return
    isBST(root.left,L)
    L.append(root.data)
    isBST(root.right,L)
    return L

def isBST2(root,minimum,maximum):
    #base case
    if not root:
        return True
    if not minimum<root.data<maximum:
        return False
    return isBST2(root.left,minimum,root.data) and isBST2(root.right,root.data,maximum)

def checkBST2(root,minimum,maximum):
    if not root:
        return True
    if not minimum<root.data<maximum:
        return False
    if checkBST2(root.left,minimum,root.data) and checkBST2(root.right,root.data,maximum):
        return True
    else:
        return False

def inorderSucc(node):
    if node.right:
        return find_min(root.right)
    parent = node.p
    curr = node
    while curr == parent.right:
        node = parent
        parent = node.p
    return parent

def find_min(node):
    while node.left:
        node = node.left
    return node


if __name__ == '__main__':
    array = [5,2,3,4,7,8,9]#range(10)
    root = minHeightTree2(array,0,len(array)-1)
    #print(checkBST2(root,-1000,1000))
    print(root)
    print(root.right)
    print(root.left)
    #tree = BST()
    #tree.insert(7)
    #tree.insert(4)
    #tree.insert(5)
    #tree.insert(6)
    #tree.insert(12)
    #tree.insert(9)
    #tree.insert(13)
    #tree.insert(10)
    #tree.insert(11)
    #tree.insert(15)
    #tree.print_tree()
    #tree.delete(6)
    #print(isBalanced(tree.root))
