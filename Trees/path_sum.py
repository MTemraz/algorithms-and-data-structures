# Question: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

def pathSum(root, value):
    if not root:
        return False
    if root.data == value and (root.left is None) and root.right is None:
        return True
    return pathSum(root.left, value-root.data) or \
      pathSum(root.right, value-root.data)

      
