class Vertex:

    def __init__(self,v):
        self.v = v
        self.connectedTo = {}
        self.color = 'white'
        self.parent = None
        self.distance = sys.maxint
        self.start_time = 0
        self.end_time = 0
        
    def addNeighbor(self,nbr,weight):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        self.distance = d

    def setParent(self,p):
        self.parent = p

    def setStartTime(self,t):
        self.start_time = t

    def setEndTime(self,t):
        self.end_time = t
        
    def __str__(self):
        return str(self.v)

class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def addVertex(self,vertex):
        v = Vertex(vertex)
        self.vertices[vertex] = v
        self.num_vertices += 1
        
    def addEdge(self,a,b,w=0):
        if a not in self.vertices:
            self.addVertex(a)
        if b not in self.vertices:
            self.addVertex(b)
        self.vertices[a].addNeighbor(self.vertices[b],w)

    def __contains__(self,v):
        return v in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())
        
if __name__ == '__main__':
    g = Graph()
    g.addVertex('USA')
    g.addVertex('Canada')
    g.addVertex('Egypt')
    g.addVertex('UK')
    g.addVertex('UAE')
    g.addVertex('France')
    g.addVertex('Brazil')
    g.addVertex('Italy')
    g.addEdge('USA','Canada',10)
    g.addEdge('USA','Egypt',100)
    g.addEdge('USA','Brazil',50)
    g.addEdge('Canada','UAE',140)
    g.addEdge('Egypt','UAE',20)
    g.addEdge('Brazil','UAE',500)
    g.addEdge('Brazil','Canada',70)
    g.addEdge('Canada','Egypt',250)
    g.addEdge('Canada','France',30)
    g.addEdge('France','UK',20)
    g.addEdge('UK','UAE',40)
    for start in g:
        for dest in start.getConnections():
            print '{0} {1} {2}'.format(start,start.getWeight(dest),dest)
