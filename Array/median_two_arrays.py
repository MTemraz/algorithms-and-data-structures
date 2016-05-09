# Question: Write code to find median of 2 sorted arrays.

def median(A,B):
    # A = [1,3,4,7,12,34]
    # B = [1,5,12,14,19]
    if len(A) == 2 and len(B)==2:
        return min(max(A[0],B[0]),min(A[1],B[1]))
    a_mid = (len(A)-1) // 2
    b_mid = (len(B)-1) //2
    if len(A) == 0:
        return B[b_mid]
    if len(B) == 0:
        return A[a_mid]
    if len(B) == 1:
        if A[a_mid] > B[0] and len(A)%2 == 0:
            return A[a_mid]
        else:
            return A[a_mid-1]
    if len(A) == 1:
        if B[b_mid] > A[0] and len(B)%2 == 0:
            return B[b_mid]
        else:
            return B[b_mid-1]
    if A[a_mid] == B[b_mid]:
        return A[a_mid]
    elif A[a_mid] > B[b_mid]:
        return median(A[:a_mid+1],B[b_mid:])
    elif A[a_mid] < B[b_mid]:
        return median(A[a_mid:],B[:b_mid+1])
