# Question: Write code to find the kth smallest element in a BST.

counter = 0
def kSmallest(root, k):
    if not root:
        return
    kSmallest(root.left)
    global counter
    counter += 1
    if counter == k:
        return root.data
    kSmallest(root.right)

def kSmallest2(root,k):
    stack = []
    stack.append(root)
    counter = 0
    while len(stack) > 0 or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            curr = stack.pop()
            counter += 1
            if counter == k:
                return curr.data
            root = curr.right
