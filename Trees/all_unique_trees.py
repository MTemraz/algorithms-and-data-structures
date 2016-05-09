class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def generateTrees(start,end):
    result = []
    if start > end:
        result.append(None)
        return result
    for i in range(start, end+1):
        left_sub = generateTrees(start, i-1)
        right_sub = generateTrees(i+1, end)
        for left_node in left_sub:
            for right_node in right_sub:
                node = TreeNode(i)
                node.left = left_node
                node.right = right_node
                result.append(node)
    return result

if __name__ == '__main__':
    n = 3
    print(generateTrees(1,n))
