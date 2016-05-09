# Question: Find the maximum sum leaf to root path in a Binary Tree. In all the paths from root to leaves, find the path which has the maximum sum


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
