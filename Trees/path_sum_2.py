# Question: Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

def allSumPaths(root, k):
    path = [root.data]
    result = []
    return dfs(root.data, k, path, result)

def dfs(root, k, path, result):
    if not root:
        return
    if root.data == k and root.left is None and root.right is None:
        result.append(path)
    if root.left:
        dfs(root.left, k-root.left.data, path+[root.left.data], result)
    if root.right:
        dfs(root.right, k-root.right.data, path+[root.right.data], result)
    return result
