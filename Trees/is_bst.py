# Question: Write code to check if a tree is a BST.

def isBST(root,result=[]):
    if not root:
        return
    isBST(root.left,result)
    result.append(root.data)
    isBST(root.right,result)
    return result == sorted(result)
