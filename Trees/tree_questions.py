from bst import *

#1 Write code to check if a tree is balanced
def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    if leftHeight==-1:
        return -1
    rightHeight = getHeight(root.right)
    if rightHeight==-1:
        return -1
    diff = leftHeight - rightHeight
    if abs(diff) > 1:
        return -1
    else:
        return max(leftHeight,rightHeight) + 1

def isBalanced(root):
    if getHeight(root):
        return True
    return False
#####################################

#2 Given a sorted array, write code to create binary_tree
#  with minimum height
def minTree(array,start,end):
    if start > end:
        return
    mid = (start+end) // 2
    root = Node(array[mid])
    root.left = minTree(array,start,mid-1)
    root.right = minTree(array,mid+1,end)
    return root

#####################################

#3 Given a binary tree, do a tree-level print
def levelTraversal(root):
    q = Queue()
    q.enqueue(root)
    curr,nxt = 1,0
    while not q.isEmpty():
        currNode = q.dequeue()
        curr -= 1
        print currNode,
        if currNode.left:
            q.enqueue(currNode.left)
            nxt += 1
        if currNode.right:
            q.enqueue(currNode.right)
            nxt += 1
        if curr == 0:
            print '\n'
            curr,nxt = nxt,curr

class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self,v):
        self.data.append(v)
    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
    def isEmpty(self):
        return len(self.data)==0
#####################################

#4 Given a binary tree, create a LinkedList of all elements
#  at each depth
def createLinkedList(root):
   result = []
   curr,nxt = 1,0
   q = Queue()
   q.enqueue(root)
   linklist = LinkedList()
   while not q.isEmpty():
       node = q.dequeue()
       curr -= 1
       linklist.insert(node.data)
       if node.left:
           nxt += 1
           q.enqueue(node.left)
       if node.right:
           nxt += 1
           q.enqueue(node.right)
       if curr == 0:
           result.append(linklist)
           linklist = LinkedList()
#####################################

#5 Write code to check if a binary tree is a BST
def checkBST(root):
    L = inorderTraversal(root)
    for i in range(1,len(L)):
        if L[i]< L[i-1]:
            return False
    return True

L = []
def inorderTraversal(root):
    if not root:
        return 
    inorderTraversal(root.left)
    L.append(root.data)
    inorderTraversal(root.right)
    return L

# Another approach
import sys
def checkBST2(root,minimum,maximum):
    if not root:
        return True
    if not minimum<root.data<maximum:
        return False
    if checkBST2(root.left,minimum,root.data) and checkBST2(root.right,root.data,maximum):
        return True
    else:
        return False
#####################################

#6 Write code to find the next node(inorder successor) in a BST
def inorderSucc(node):
    if not node:
        return None
    if node.right:
        return find_min(node.right)
    parent = node.p
    while parent and node==parent.right:
        parent = parent.p
        node = parent
    return parent
#####################################

#7 Write code to find the first common ancestor of two nodes 
#  in a binary tree
def sameSide(root,node):
    if not root:
        return False
    if root is node:
        return True
    return sameSide(root.left) or sameSide(root.right)

def getAncestor(root,a,b):
    if not root:
        return None
    if root is a or root is b:
        return root
    a_is_left = sameSide(root.left,a)
    b_is_left = sameSide(root.left,b)
    if a_is_left != b_is_left:
        return root
    side = root.left if a_is_left else root.right
    return getAncestor(side,a,b)

