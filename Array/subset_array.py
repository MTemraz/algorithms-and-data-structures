# Question: Write code to check if one array is subset of another, without using extra space.

def isSubset(A,B):
    if len(A) < len(B):
        return False
    A.sort()
    b.sort()
    ia = 0
    ib = 0
    while ia < len(A) and ib < len(B):
        if A[ia] == B[ib]:
            ia += 1
            ib += 1
        elif A[ia] > B[ib]:
            return False
        elif A[ia] < B[ib]:
            ia += 1
    return True
