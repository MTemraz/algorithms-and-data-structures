class Heap:
    def __init__(self,array=None):
        if not array:
            self.data = []
        else:
            self.data = array
            for i in reversed(range(len(self.data)//2)):
                percolate_down(self.data,i)

    def insert(self,data):
        self.data.append(data)
        percolate_up(self.data,len(self.data)-1)

    def extractMin(self):
        min = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        percolate_down(self.data,0)
        return min

def percolate_down(L,i):
    left  = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < len(L) and L[left] > L[largest]:
        largest = left
    if right < len(L) and L[right] > L[largest]:
        largest = right
    if largest != i:
        L[i],L[largest] = L[largest],L[i]
        percolate_down(L,largest)

def percolate_up(L,i):
    parent = i-1 //2
    if parent >= 0 and L[parent] < L[i]:
        L[i],L[parent] = L[parent],L[i]
        percolate_up(L,parent)
