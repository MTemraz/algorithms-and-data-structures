class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,v):
        if self.root is None:
            self.root = Node(v)
        else:
            _insert(self.root,v)
            
    def delete(self,v):
        if self.root is None:
            return 
        self.root = _delete(self.root,v)

    def contains(self,v):
        if self.root is None:
            return False
        return _contains(self.root,v)
    
    def print_tree(self):
       draw_tree(self.root, 1)

    def traverse(self):
        _traverse(self.root)

def _traverse(root):
    if not root:
        return
    _traverse(root.left)
    print(root.data)
    _traverse(root.right)

def draw_tree(root, depth):
   if root is None:
       return
   draw_tree(root.right, depth + 1)
   print("    " * (depth - 1) + str(root))
   draw_tree(root.left, depth + 1)

def _contains(root,v):
    if not root:
        return False
    if root.data == v:
        return True
    elif v > root.data:
        return _contains(root.right,v)
    else:
        return _contains(root.left,v)

def _delete(root,v):
    if root.data == v:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            pred = find_max(root.left)
            root.data = pred.data
            root.left = _delete(root.left,pred.data)
            return root
    else:
        if v > root.data:
            root.right = _delete(root.right,v)
        else:
            root.left = _delete(root.left,v)
        return root

def find_max(node):
    while node.right:
        node = node.right
    return node

def _insert(root,v):
    if v > root.data:
        if root.right is None:
            root.right = Node(v)
        else:
            _insert(root.right,v)
    else:
        if root.left is None:
            root.left = Node(v)
        else:
            _insert(root.left,v)

if __name__ == '__main__':
    tree = BST()
    tree.insert(7)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(12)
    tree.insert(9)
    tree.insert(13)
    tree.insert(10)
    tree.insert(11)
    tree.insert(15)
    tree.print_tree()
    tree.delete(7)
    tree.print_tree()
