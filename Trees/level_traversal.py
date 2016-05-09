# Question: Given a binary tree, do a level order traversal.

def levelTraversal(root):
    cache = Queue()
    cache.enqueue(root)
    curr,nxt = 1,0
    while not cache.isEmpty():
        curr_node = cache.dequeue()
        curr -= 1
        print(curr_node.data,)
        if curr_node.left:
            cache.enqueue(curr_node.left)
            nxt += 1
        if curr_node.right:
            cache.enqueue(curr_node.right)
            nxt += 1
        if curr == 0:
            print('\n')
            curr,nxt = nxt,curr

class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self,x):
        self.data.append(x)
    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
    def isEmpty(self):
        return len(self.data) == 0
