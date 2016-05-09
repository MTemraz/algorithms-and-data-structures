# Question: Get nth fibonacci number

def bottomUp(n):
    fib = [0 for _ in range(n+1)]
    fib[0] = 1
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def topDown1(n,fib={0:1,1:1}):
    if n in fib:
        return fib[n]
    fib[n] = topDown1(n-1,fib) + topDown1(n-2,fib)
    return fib[n]


def topDown2(n, fib={0:1,1:1}):
    if n not in fib:
        fib[n] = topDown1(n-1,fib) + topDown1(n-2,fib)
    return fib[n]
    
