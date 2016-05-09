# Question: write code to find the next node (inorder successor) in a BST.

def inorderSuccessor(root):
    if not root:
        return
    if root.right:
        return findMin(root.right)
    parent = root.p
    curr = root
    while parent and curr == parent.right:
        curr = parent
        parent = parent.p
    return parent
