# Question: Write code to check if a tree is balanced.

def isBalanced(root):
    if getHeight(root):
        return True
    return False

def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    if leftHeight == -1:
        return False
    rightHeight = getHeight(root.right)
    if rightHeight == -1:
        return False
    diff = leftHeight - rightHeight
    if abs(diff) > 1:
        return -1
    return max(leftHeight,rightHeight)+1
