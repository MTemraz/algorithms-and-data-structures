class Node:
    def __init__(self,data,l=None,r=None):
        self.data = data
        self.left = l
        self.right = right

class BST:
    def __init__(self,root=None):
        self.root = root

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            _insert(self.root,data)

    def delete(self,data):
        if not self.root:
            return
        self.root = _delete(self.root,data)

def _delete(root,data):
    if root.data == data:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        else:
            inorder_succ = find_max(root.left)
            root.data = inorder_succ.data
            _delete(root.left,inorder_succ.data)
            return root
    else:
        if root.data < data:
            root.right = _delete(root.right,data)
        else:
            root.left = _delete(root.left,data)
        return root
        

def _insert(root,data):
    if data > root.data:
        if not root.right:
            root.right = Node(data)
        else:
            _insert(root.right.data)
    else:
        if not root.left:
            root.left = Node(data)
        else:
            _insert(root.left,data)
