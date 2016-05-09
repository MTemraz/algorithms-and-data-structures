# Question: Write code to find the next greater element for each element in the array.

def nextGreater(array):
    # array = [11,12,6,13]
    stack = list()
    stack.append(array[0])
    for i in range(1,len(array)):
        nxt = array[i]
        curr = stack.pop()
        while nxt > curr:
            print (curr,nxt)
            if len(stack) == 0:
                break
            curr = stack.pop()
        if curr > nxt:
            stack.append(curr)
        stack.append(nxt)
    for i in stack:
        print (i,-1)
