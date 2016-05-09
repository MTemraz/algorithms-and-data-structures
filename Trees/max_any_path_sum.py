# Question: Write code to find the maximum path sum in a tree. The path can start anywhere and end anywhere.

def maxAnyPathSum(root, max_sum):
    if not root:
        return 0
    leftS = maxAnyPathSum(root.left, max_sum)
    rightS = maxAnyPathSum(root.right, max_sum)
    curr_sum = max(root.data, max(root.data+leftS, root.data+rightS))
    max_sum[0] = max(max_sum[0], max(curr_sum, root.data+leftS+rightS))
    return curr_sum

