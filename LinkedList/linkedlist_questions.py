'''
Description: LinkedList related questions
@author: Temraz
@email: temraz@cens.io
'''

from linkedlist import *

# 1 Write code to reverse a LinkedList
def reverseLL(link_list):
    last = None
    curr = link_list.head
    head = link_list.tail
    link_list.head = head
    link_list.tail = curr
    while curr is not None:
        nxt = curr.next
        curr.next = last
        last,curr = curr,nxt

#####################################

# 2 Write code to sort a LinkedList
def mergeSortLL(head):
    if head.next is None:
        return head
    mid = getMiddle(head)
    secHalf = mid.next
    mid.next = None
    return merge(mergeSortLL(head),mergeSortLL(secHalf))

def merge(a,b):
    dummy = LLNode()
    curr = dummy
    while (a is not None) and (b is not None):
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
    return dummy.next

def getMiddle(head):
    slow = head
    fast = head
    if head is None:
        return head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#####################################

#3 Write code to remove duplicates from a LinkedList
def removeDups(head):
    cache = {}
    prev = LLNode()
    while head is not None:
        if head.data in cache:
            prev.next = head.next
        else:
            cache[head.data] = True
            prev = head
        head = head.next

#####################################

#4 Write code to find the nth to last element in a LinkedList
def nthLast(head,n):
    fast = head; slow=head
    for _ in xrange(n):
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow.data
    
#####################################

#5 Delete a node in a LinkedList given access only to that node
def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next

#####################################

#6 Write code to partition a LinkedList around a value
def partition(array,value):
    less = LinkedList()
    more = LinkedList()
    for e in array:
        if e <= value:
            less.addLast(e)
        else:
            more.addLast(e)
    less.tail.next = more.head
    return less.head

#####################################

#7 Write code to add two number represented as LinkedLists
#  and return their sum as a LinkedList also
#  ex: 6->1->7 + 5->1->1 = 1->3->8 which is equivalent to
#  716 + 115 = 831
def addLists(List1,List2):
    if size(List1.head) != size(List2.head):
        adjust(List1,List2)
    a = List1.head; b = List2.head
    carry = 0
    result = LinkedList()
    while (a is not None) and (b is not None):
        currentSum = a.data + b.data + carry
        if currentSum > 10:
            carry = 1
            if a.next is not None:
                result.addLast(currentSum%10)
            else:
                result.addLast(currentSum)
        else:
            carry = 0
            result.addLast(currentSum)
        a = a.next
        b = b.next
    return result.head
        
def size(node):
    counter = 0
    while node is not None:
        counter += 1
        node = node.next
    return counter

def adjust(L1,L2):
    if size(L1.head) > size(L2.head):
        smaller = L2
        larger = L1
    else:
        smaller = L1
        larger = L2
    for _ in xrange(size(smaller.head),size(larger.head)):
        smaller.addFirst(0)

#####################################

#8 Write code to find node at the beginning of a circular LinkedList
def findNode(node):
    slow = node
    fast = node
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    slow = node
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return slow

#####################################

#9 Check if a LinkedList is a palindrome
def isPalindrome(node):
    mid = getMiddle(node)
    secHalf = reverse(mid)
    while secHalf is not None:
        if node.data != secHalf.data:
            return False
        node = node.next
        secHalf = secHalf.next
    return True

def reverse(node):
    last = None
    curr = node
    while curr is not None:
        nxt = curr.next
        curr.next = last
        last,curr = curr,nxt
    return last

#####################################
