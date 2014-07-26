import random

def qS(L,start,end):
    if start<end:
        q = partition(L,start,end)
        qS(L,start,q-1)
        qS(L,q+1,end)

def partition(L,start,end):
    rand_num = random.randint(start,end)
    L[rand_num],L[end] = L[end],L[rand_num]
    pivot = L[end]
    less = start-1
    for i in range(start,end):
        if L[i] <= pivot:
            less += 1
            L[less],L[i]=L[i],L[less]
    L[less+1],L[end] = L[end],L[less+1]
    return less+1

if __name__ == '__main__':
    L = [10,-2,3,1,0,4,2]
    print L
    qS(L,0,len(L)-1)
    print L
