class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def addVertex(self,id):
        self.vertices[id] = Vertex(id)

    def addEdge(self,source,target,weight):
        if source not in self.vertices:
            self.addVertex(source)
        if target not in self.vertices:
            self.addVertex(target)
        self.vertices[source].addNeighbour(self.vertices[target], weight)

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self,id):
        return id in self.vertices

def bfs(graph,start):
    queue = Queue()
    for v in graph.vertices:
        v.setDistance(0)
        v.setColor('white')
    start.setColor('grey')
    queue.enqueue(start)
    while not queue.isEmpty():
        curr = queue.dequeue()
        for nbr in curr.getConnections():
            if nbr.color == 'white':
                nbr.setColor('grey')
                nbr.setParent(curr)
                nbr.setDistance(curr.distance+1)
                q.enqueue(nbr)
        curr.setColor('black')

time = 0
def dfs(graph,start):
    for v in graph.vertices:
        if v.color == 'white':
            dfs_visit(v)

def dfs_visit(v,time):
    time += 1
    v.setStartTime(time+1)
    v.setColor('grey')
    for nbr in v.getConnections():
        if nbr.color == 'white':
            dfs_visit(nbr)
    time += 1
    v.setColor('black')
    v.setEndTime(time)

def dijkstra(graph,source,target):
    source.setDistance(0)
    pq = PriorityQueue()
    for v in graph.vertices:
        pq.enqueue(v)
    while not pq.isEmpty():
        curr = pq.extractMin()
        for v in curr.getConnections():
            if v.distance > curr.distance + curr.getWeight(nbr):
                v.setDistance(curr.distance + curr.getWeight(nbr))
                v.setColor('grey')
                pq.decreaseKey(v,v.distance)
