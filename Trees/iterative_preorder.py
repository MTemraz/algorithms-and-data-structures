def iterativePreorder(root):
    stack = [root]
    result = []
    while len(stack) > 0:
        curr = stack.pop()
        result.append(curr)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result
