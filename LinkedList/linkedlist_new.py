class LLNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        node = LLNode(data)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def setHead(self,data):
        node = LLNode(data)
        if not self.tail:
            self.tail = node
        node.next = self.head
        self.head = node

            
    def removeFirst(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def removeLast(self):
        if not self.head:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.tail = curr
