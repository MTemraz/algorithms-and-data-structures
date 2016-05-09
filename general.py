cache = {}
def wordBreak(string,words):
    if string in words:
        return string
    if string in cache:
        return cache[string]
    for i in range(1,len(string)+1):
        prefix = string[:i]
        if prefix in words:
            remaining = wordBreak(string[i:])
            if remaining:
                return prefix+" "+remaining
    cache[string] = True

def allPrimes(n):
    import math
    cache = range(n)
    cache[1] = 0
    stop = int(math.sqrt(n))+1
    for i in xrange(2,stop):
        if cache[i]:
            cache[i*i:n:i] = [False]*len(range(i*i,n,i))
    return filter(lambda x: x, cache)

def reverseInt(num):
    # num = 123
    result = 0
    while num != 0:
        end = num % 10
        result = result*10 + end
        num = num // 10
    return result

def addNums(a,b):
    # 2 -> 010
    # 3 -> 011
    if b == 0:
        return a
    sum = a^b
    carry = a&b << 1
    return addNums(sum,carry)

def power(a,b):
    if b == 1:
        return a
    if b%2 == 0:
        return power(a*a,b/2)
    return a*power(a,b-1)

def fibonacci(n,cache={0:0,1:1}):
    if n not in cache:
        cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
    return cache[n]

def fib2(n):
    cache = {}
    if n in cache:
        return cache[n]
    if n <= 2:
        f = 1
    else:
        f = fibonacci(n-1)+fibonacci(n-2)
    cache[n] = f
    return f
        
def sqrt(n):
    pass

def LL_BST(head):
    # O(nlogn)
    mid = getMid(head)
    temp = mid.next
    mid.next = None
    node = BSTNode(mid.data)
    node.left = LL_BST(head)
    node.right  = LL_BST(temp)
    return node

def LL_BST(head):
    # O(n)
    pass

def prodMinusSelf(array):
    # x = [10,3,8,2,4]
    temp = 1
    prod = [0 for _ in x]
    for i in range(len(x)):
        prod[i] = temp
        temp *= array[i]
    temp = 1
    for i in reversed(range(len(array))):
        prod[i] *= temp
        temp *= array[i]
    return prod

def isPalindrome(num):
    pass


counter = 0
def kSmallestBST(root,k,L=[]):
    if root is None or counter >= k:
        return None
    kSmallestBST(root.left,k,L)
    global counter
    counter += 1
    if counter == k:
        print root.data
    kSmallestBST(root.right,k,L)
    
def wordBreak(string,dictionary):
    if string in dictionary:
        return string
    if string in cache:
        return cache[string]
    for i in range(1,len(string)):
        prefix = string[:i]
        if prefix in dictionary:
            remaining = wordBreak(string[i:])

def minCostPath(matrix):
    # matrix = [[1,2,3]
    #           [4,5,6]]
    DP = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    for i in range(1,len(matrix[0])):
        DP[0][i] = DP[0][i-1] + matrix[0][i]
    for j in range(1,len(matrix)):
        DP[j][0] = DP[j-1][0] + matrix[j][0]
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            DP[i][j] = matrix[i][j] + min(DP[i-1][j],DP[i][j-1])
    return DP[-1][-1]

def numberPaths(matrix):
    # matrix = [[1,2,3]
    #           [4,5,6]]
    rows = len(matrix)
    columns = len(matrix[0])
    DP = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        DP[i][0] = 1
    for j in range(columns):
        DP[0][j] = 1
    for i in range(1,rows):
        for j in range(1,columns):
            DP[i][j] = DP[i-1][j] + DP[i][j-1]
    return DP[-1][-1]

def rotateMatrix(matrix):
    pass

def longestPalin(string):
    start = 0
    end = 0
    for i in range(len(string)):
        left = i
        right = i
        while left>=0 and right<len(string):
            if string[left] == string[right]:
                if right-left > end-start:
                    start = left
                    end = right
                left -= 1
                right += 1
        return string[start:end+1]

def topKWords(words):
    pass

def 4Sum(array):
    pass

def validParans(n):
    left = n
    right = n
    return _validParans(left,right,'',[])

def _validParans(left,right,string,result):
    if left < 0 or right < left:
        return
    if left == 0 and right == 0:
        result.append(string)
    if left > 0:
        _validParans(left-1,right,string+'(',result)
    if right > left:
        _validParans(left, right-1, string+')',result)
    return result

def countingSort(A):
    # A = [0,3,4,2,10,9]
    max_num = max(A)
    B = [0 for i in range(max_num+1)]
    C = [0] * len(A)
    for i in range(len(A)):
        B[A[i]] += 1
    for i in range(1,len(B)):
        B[i] += B[i-1]
    for i in range(len(C)):
        C[B[A[i]]-1] = A[i]
        B[A[i]] -= 1
    return C

def isSubset(A,B):
    pass

def maxProfit(array):
    # array = [10,3,5,9,5,6,0]
    max_profit = 0
    curr_profit = 0
    start = 0
    end = 0
    t_start = 0
    for i in range(1,len(array)):
        curr = array[i] - array[t_start]
        if curr > curr_profit:
            curr_profit = curr
        else:
            t_start = i
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = t_start
            end = i
    return max_profit,start,end

def longestContinSum(array):
    curr_sum = array[0]
    max_sum  = array[0]
    start = 0
    end = 0
    t_start = 0
    for i in range(1,len(array)):
        if array[i] > curr_sum + array[i]:
            curr_sum = array[i]
            t_start = i
        else:
            curr_sum += array[i]
        

def maxBooking(array):
    # array = [1,3,6,2]
    # cache = [1,3,7,7]
    cache = [0 for _ in range(len(array))]
    cache[0] = array[0]
    cache[1] = array[1]
    for i in range(2,len(array)):
        cache[i] = max(cache[i-1], cache[i-2]+array[i])
    return cache[-1]

def sumMinusSelf(array):
    # array = [1,4,2,3,5]
    # cache = [0,1,5,7,10]
    cache = [0 for _ in range(len(array))]
    for i in range(1,len(array)):
        cache[i] = cache[i-1] + array[i-1]
    temp = 0
    for i in reversed(range(len(array))):
        cache[i] += temp
        temp += array[i]
    return cache

def repeatElement(array):
    # array = [1,3,6,1,4]
    # count_array = [0,-1,0,-3,0,0,-6]
    cache = [0 for _ in range(len(array))]
    

def subsetSum(array,n):
    cache = [[0]*(n+1) for _ in range(len(array)+1)]
    for i in range(len(array)+1):
        cache[i][0] = True
    for i in range(n+1):
        cache[0][i] = False
    for i in range(1,len(array)):
        for j in range(1,n):
            if i >= array[j-1]:
                cache[i][j] = cache[i-1][j] or cache[i-1][j-array[i-1]]
    return cache[-1][-1]

def editDistance(a,b):
    # a = intention
    # b = execution
    #replace = DP[i][j] + 1
    #delete = DP[i+1][j] + 1
    #insert = DP[i][j+1] + 1

def maxBooking(array):
    # a = [1,3,1,3]
    # cache = [1,3,,]
    cache = [0] * len(array)
    cache[0] = 2
    cache[1] = max(a[0],a[1])
    for i in range(2,len(array)):
        cache[i] = max(cache[i-1], cache[i-2] + array[i])
    return cache[-1]



def longestContinuousSubset(array):
    # array = [20,19,21,3,5,4,6,8]
    cache = {num:True for num in array}
    max = 1
    subset_start = array[0]
    for num in array:
        count = 1
        start = num
        left = num - 1
        right = num + 1
        while left in cache:
            count += 1
            start = left
            del cache[left]
            left -= 1
        while right in cache:
            count += 1
            del cache[right]
            right += 1
        if count > max:
            max = count
            subset_start = start
    result = [subset_start]
    for _ in range(max-1):
        subset_start += 1
        result.append(subset_start)
    return result


def allPermutations(string, perm='', result=[]):
    if len(string) == 0:
        result.append(perm)
    for i in range(len(string)):
        char = string[i]
        remaining = string[:i]+string[i+1:]
        allPermutations(remaining, perm+char, result)
    return result

def validParans(n):
    left_remain = n
    right_remain = n
    result = []
    _validParans(left_remain, right_remain, result, '')
    return result

def _validParans(left, right, result, temp):
    if left == 0 and right == 0:
        result.append(temp)
    if left < 0 and right < 0:
        return
    if left > 0:
        _validParans(left-1, right, result, temp+'(')
    if right > left:
        _validParans(left, right-1, result, temp+')')

def balancedParans(string):
    # (()))
    cache = []
    for letter in string:
        if letter == '(':
            cache.append(letter)
        else:
            if len(cache) > 0:
                last = cache.pop()
                if last != '(':
                    return False
            else: return False
    return len(cache) == 0

def longIncSubsequence(array):
    # [10, 9, 2, 5, 3, 7, 101, 18], result = [2, 3, 7, 101]
    if not array: return
    cache = [1 for _ in array]
    for i in range(len(array)):
        for j in range(i):
            if array[i] > array[j]:
                cache[i] = max(cache[i], cache[j]+1)
    max_value =  max(cache)
    max_index = cache.index(max_value)
    result = []
    while max_index >= 0:
        if cache[max_index] == max_value:
            result.append(array[max_index])
            max_value -= 1
        max_index -= 1
    return result

def isConsecutive(array):
    # array = [21,24,22,26,23,25]
    maximum, minimum = max(array), min(array)
    if len(array) != maximum-minimum+1:
        return False
    temp = [0 for _ in array]
    for element in array:
        idx = element-minimum
        if temp[idx] != 0:
            return False
        temp[idx] = 1
    return True

def equilibriumIndex(array):
    # array = [-7,1,5,2,-4,3,0]
    # array = [1,2,3,4,6]
    total = sum(array)
    left_sum = 0
    for i in range(len(array)):
        total -= array[i]
        if left_sum == total:
            return i
        left_sum += array[i]
        print left_sum,total
        

def kSmallest(array, start, end, k):
    q = partition(array, start, end)
    i = q-start+1
    if i == k:
        return array[i]
    elif i < k:
        return kSmallest(array, q+1, end, k-i)
    else:
        return kSmallest(array, start, q-1, k)


    
def longContSubset(array):
    # [20,19,21,3,5,4,6,8]
    cache = {}
    longest = 0
    final_start = 0
    final_end = 0
    for num in array:
        cache[num] = True
    for i in range(len(array)):
        curr = array[i]
        curr_length = 1
        left = curr - 1
        right = curr + 1
        start = i
        while left in cache:
            start  = left
            curr_length += 1
            del cache[left]
            left -= 1
        while right in cache:
            curr_length += 1
            del cache[right]
            right += 1
        if curr_length > longest:
            final_start = start
            final_end = right - 1
            longest = curr_length
    return range(final_start, final_end+1)


def removeDups(array):
    # array = [3,3,4,5,5,5,6]
    slow = 0
    fast = 1
    while fast < len(array):
        if array[slow] == array[fast]:
            fast += 1
        else:
            slow += 1
            array[slow] = array[fast]
            fast += 1
    return array[:slow+1]

def addDigits(a, b):
    if b == 0:
        return a
    sum = a ^ b
    carry = (a & b) << 1
    return addDigits(sum, carry)
