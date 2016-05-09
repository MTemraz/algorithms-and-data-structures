def hS(L):
    max_heapify(L)
    i = len(L)-1
    while i > 0:
        L[0],L[i] = L[i],L[0]
        percolate_down(L,0,i)
        i -= 1

def max_heapify(L):
    i = len(L)//2 - 1
    n = len(L)
    while i >= 0:
        percolate_down(L,i,n)
        i -= 1

def percolate_down(L,i,n):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < n and L[left] > L[largest]:
        largest = left
    if right < n and L[right] > L[largest]:
        largest = right
    if largest != i:
        L[i],L[largest] = L[largest],L[i]
        percolate_down(L,largest,n)
