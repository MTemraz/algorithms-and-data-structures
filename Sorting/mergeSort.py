def mS(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    a = mS(L[:mid])
    b = mS(L[mid:])
    ia = 0
    ib = 0
    result = []
    while ia < len(a) or ib < len(b):
        if ia < len(a) and ib < len(b):
            if a[ia] < b[ib]:
                result.append(a[ia])
                ia += 1
            else:
                result.append(b[ib])
                ib += 1
        elif ia < len(a):
            result.extend(a[ia:])
            break
        elif ib < len(b):
            result.extend(b[ib:])
            break
    return result
