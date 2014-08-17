# Single-source shortest path: Dijkstra's algorithm
from graph import *

def dijkstra(start,graph):
    pq = PriorityQueue()
    start.setDistance(0)
    for v in graph:
        pq.insert(v)
    while not pq.isEmpty():
        curr = pq.extractMin()
        for nbr in curr.getConnections():
            if nbr.distance > curr.distance + curr.getWeight(nbr):
                nbr.setParent(curr)
                val = curr.distance+curr.getWeight(nbr)
                pq.decreaseKey(nbr,val)

class PriorityQueue:
    '''min-heap implementation to store graph vertices'''
    def __init__(self):
        self.data = []

    def insert(self,obj):
        self.data.append(obj)
        percolate_up(self.data,len(self.data)-1)

    def extractMin(self):
        root = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        percolate_down(self.data,0)
        return root

    def decreaseKey(self,obj,new_val):
        key = find_index(self.data,obj)
        self.data[key].setDistance(new_val)
        percolate_up(L,key)
        
def find_index(L,element):
    for i in range(len(L)):
        if L[i] is element:
            return i
        
def percolate_up(L,i):
    parent = i-1 // 2
    if i >= 0 and L[parent] > L[i]:
        L[i],L[parent] = L[parent],L[i]
        percolate_up(L,parent)

def percolate_down(L,i):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i
    if left<len(L) and L[left].distance < L[smallest].distance:
        smallest = left
    if right<len(L) and L[right].distance < L[smallest].distance:
        smallest = right
    if smallest != i:
        L[smallest],L[i] = L[i],L[smallest]
        percolate_down(L,smallest)
    
