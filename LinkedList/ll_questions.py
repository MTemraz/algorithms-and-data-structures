def reverseLL(head):
    # 1->2->3->4-None
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        curr,prev = temp,curr
    return prev

def isPalindrome(head):
    # 5->4->1->4->5
    mid = getMid(head)
    sec_half = reverseMid(mid)
    while secHalf is not None:
        if head.data != secHalf.data:
            return False
        head = head.next
        secHalf = secHalf.next
    return True

def getMid(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def nToLast(head,n):
    # 1->2->3->4->5
    fast = head
    slow = head
    for _ in range(n): fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow.data

def removeDups(curr):
    # 1->2->4->2->2
    cache = {}
    prev = LLNode()
    while curr:
        if curr.data not in cache:
            prev.next = curr
            cache[curr.data] = True
        curr = curr.next
        
def mergeSortLL(head):
    if head.next is None:
        retrurn head
    mid = getMid(head)
    sec_half = mid.next
    mid.next = None
    return merge(mergeSortLL(head),mergeSortLL(sec_half))

def merge(a,b):
    result = LLNode()
    curr = result
    while a is not None and b is not None:
        if a.data < b.data:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    if a is not None:
        curr.next = a
    else:
        curr.next = b
    return result.next
    
