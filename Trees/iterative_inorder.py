def iterativeInorder(root):
    stack = list()
    #stack.append(root)
    #root = root.left
    result = []
    while len(stack) > 0 or root is not None:
        if root:
            stack.append(root)
            root = root.left
        else:
            curr = stack.pop()
            result.append(curr)
            root = curr.right
    return result
            
