# Question: Merge 2 sorted arrays.

def mergeSorted(a,b):
    result = []
    ia = 0
    ib = 0
    while ia < len(a) and ib < len(b):
        if a[ia] >= b[ib]:
            result.append(b[ib])
            ib += 1
        elif a[ia] < b[ib]:
            result.append(a[ia])
            ia += 1
    if ia < len(a):
        result.extend(a[ia:])
    if ib < len(b):
        result.extend(b[ib:])
    return result
            
