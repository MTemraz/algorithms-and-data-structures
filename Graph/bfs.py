# Write code to implement Breadth First Search given a node in a Graph

def bfs(start):
    start.setColor('grey')
    start.setDistance(0)
    q = Queue()
    q.enqueue(start)
    while not q.isEmpty():
        curr = q.dequeue()
        print curr,
        for v in curr.getConnections():
            if v.color == 'white':
                v.setParent(curr)
                v.setColor('grey')
                v.setDistance(curr.distance+1)
                q.enqueue(v)
        curr.setColor('black')
        
class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self,element):
        self.data.append(element)
    def dequeue(self):
        return self.data.pop(0)
    def isEmpty(self):
        return len(self.data) == 0
