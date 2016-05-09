# Question: Write code to find the minimum depth of a binary tree.

def minDepth(root,level=0,shortest=[1000],shortest_path=[None],path=[]):
    if not root:
        return
    level += 1
    if not root.left and not root.right:
        if level < shortest[0]:
            shortest[0] = level
            shortest_path[0] = path+[root.data]
    minDepth(root.left,level,shortest,shortest_path,path+[root.data])
    minDepth(root.right,level,shortest,shortest_path,path+[root.data])
    return shortest[0],shortest_path[0]

def minDepth2(root):
    queue = Queue()
    queue.enqueue(root)
    curr = 1
    nxt = 0
    depth = 0
    while not queue.isEmpty():
        node = queue.dequeue()
        curr -= 1
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.enqueue(node.left)
            nxt += 1
        if node.right:
            queue.enqueue(node.right)
            nxt += 1
        if curr == 0:
            depth += 1
            curr = nxt
            nxt = 0
