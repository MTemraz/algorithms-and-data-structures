# Question: Write code to find the maximum sum between any two leaves in a tree

def maxLeafToLeafSum(root, max_sum):
    if not root:
        return 0
    leftSum = maxLeafToLeafSum(root.left)
    rightSum = maxLeafToLeafSum(root.right)
    if leftSum == 0 and rightSum == 0:
        curr_sum = root.data
    else:
        curr_sum = max(leftSum+rightSum+root.data, max(leftSum,rightSum))
        if curr_sum > max_sum[0]:
            max_sum[0] = curr_sum
    return max(leftSum,rightSum)+root.data
    
