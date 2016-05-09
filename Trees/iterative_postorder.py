def iterativePostorder1(root):
    stack = list()
    prev = None
    stack.append(root)
    result = []
    while len(stack) > 0:
        curr = stack[-1]
        if prev is None or prev.left == curr or prev.right == curr:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
            else:
               node = stack.pop()
               result.append(node.data)
        elif curr.left == prev:
            if curr.right:
                stack.append(curr.right)
            else:
                node = stack.pop()
                result.append(node.data)
        elif curr.right == prev:
            node = stack.pop()
            result.append(node.data)
        prev = curr
    return result
            

# using 2 stacks
def iterativePostorder2(root):
    stack1 = list()
    stack2 = list()
    stack1.append(root)
    while len(stack1) > 0:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    return list(reversed(stack2))
