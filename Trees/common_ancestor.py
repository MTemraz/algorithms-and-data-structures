# Question: Write code to find the first common ancestor of two nodes.

def commonAncestor(root,a,b):
    if not root:
        return 
    if root is a or root is b:
        return root
    is_a_right = getSide(root.right,a)
    is_b_right = getSide(root.right,b)
    if is_a_right != is_b_right:
        return root
    if is_a_right is True:
        return commonAncestor(root.right,a,b)
    return commonAncestion(root.left,a,b)

def getSide(root,node):
    if not root:
        return
    if root is node:
        return True
    return getSide(root.left,node) or getSide(root.right,node)
