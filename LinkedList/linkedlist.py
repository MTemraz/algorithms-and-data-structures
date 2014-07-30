class LLNode:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next is not None:
            return str(self.data)+'->'+str(self.next)
        return str(self.data)

class LinkedList:

    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def addFirst(self,v):
        node = LLNode(v,self.head)
        if not self.tail:
            self.tail = node
        self.head = node

    def addLast(self,v):
        node = LLNode(v)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def removeFirst(self):
        if self.tail is not None:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def removeLast(self):
        if self.tail is not None:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                self.tail = curr
                curr.next = None
