class Vertex:
    def __init__(self,v):
        self.v = v
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight):
        self.conectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def addVertex(self, vertex):
        v = Vertex(vertex)
        self.vertices[vertex] = v
        self.num_vertices += 1

    def addEdge(self,a,b,weight):
        if a not in self.vertices:
            self.addVertex(a)
        if b not in self.vertices:
            self.addVertex(b)
        self.vertices[a].addNeighbour(self.vertices[b], weight)
        
    def __iter__(self):
        return iter(self.vertices.values())
