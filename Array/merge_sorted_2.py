# Question: Merge 2 sorted arrays A and B, assuming A has a large buffer in the end.

def mergeSorted2(a,b):
    k = len(a) + len(b) - 1
    ia = len(a)-1
    ib = len(b)-1
    while ia >= 0 and ib >= 0:
        if a[ia] > b[ib]:
            a[k] = a[ia]
            ia -= 1
        else:
            a[k] = b[ib]
            ib -= 1
        k -= 1
    if ia >= 0:
        a[:k+1] = a[:ia+1]
    if ib >= 0:
        a[:k+1] = b[:ib+1]
