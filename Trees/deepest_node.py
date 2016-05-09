# Question: Given a binary tree, find the deepest node in it.

def deepestNode(root, level=0, deepest=[0], node=[None]):
    if not root:
        return
    level += 1
    if root.left is None and root.right is None:
        if level > deepest[0]:
            deepest[0] = level
            node[0] = root.data
    deepestNode(root.left,level,deepest,node)
    deepestNode(root.right,level,deepest,node)
    return deepest[0], node[0]
