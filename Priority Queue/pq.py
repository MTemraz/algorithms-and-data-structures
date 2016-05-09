# A slight modification of the Heap implementation.
# This is a min priority queue where 

class PriorityQueue:

    def __init__(self,data=None):
        if data is None:
            self.data = []
        else:
            self.data = data
            for i in reversed(range(len(data)//2)):
                percolate_down(self.data,i)

    def insert(self,element):
        self.data.append(element)
        percolate_up(self.data,len(self.data)-1)

    def extractMin(self):
        self.data[0] = self.data[-1]
        self.data.pop()
        percolate_down(self.data,0)

    def decreaseKey(self,key,new_value):
        index = self.data.index(key)
        self.data[index][1] = new_value
        percolate_up(self.data,index)

    def increaseKey(self,key,new_value):
        index = self.data.index(key)
        self.data[index][1] = new_value
        percolate_down(self.data,index)
        
def percolate_up(L,i):
    parent = (i-1) // 2
    if parent >= 0 and L[parent][1] > L[i][1]:
        L[parent],L[i] = L[i],L[parent]
        percolate_up(L,parent)
        
def percolate_down(L,i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < len(L) and L[left][1] < L[largest][1]:
        largest = left
    if right < len(L) and L[right][1] < L[largest][1]:
        largest = right
    if largest != i:
        L[largest],L[i] = L[i],L[largest]
        percolate_down(L,largest)
