class Heap:
    
    Def __init__(self,data=None):
        if data is None:
           self.data = []
        else:
            for i in reversed(range(len(data)//2)):
                self.percolate_down(data,i)

    def insert(self,v):
        self.data.append(v)
        percolate_up(self.data,len(self.data)-1)

    def delete(self):
        self.data[0] = self.data[-1]
        self.data.pop()
        percolate_down(self.data,0)

def percolate_up(L,i):
    parent = i-1 // 2
    if  parent >= 0 and L[parent] < L[i]:
        L[i],L[parent] = L[parnet],L[i]
        percolate_up(L,parent)
                
def percolate_down(L,i):
    left = 2*i + 1
    right = 2*i +2
    largest = i
    if left < len(L) and L[left] > L[largest]:
          largest=left
    if right < len(L) and L[right] > L[largest]:
        largest = right
    if largest != i:
        L[i],L[largest] = L[largest],L[i]
        percolate_down(L,largest)



    
