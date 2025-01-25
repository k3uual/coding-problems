class node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
    
def insert(vertex, val):
    if vertex is None:
        return node(val)
    if vertex.data == val:
        return vertex 
    if vertex.data < val:
        vertex.right = insert(vertex.right, val)
    else:
        vertex.left = insert(vertex.left, val)
    return vertex 
    
def inorder(vertex):
    if vertex is None: return
    inorder(vertex.left)
    print(vertex.data, end=" ")
    inorder(vertex.right)

def preorder(vertex):
    if vertex is None: return
    print(vertex.data, end=" ")
    preorder(vertex.left)
    preorder(vertex.right)

def postorder(vertex):
    if vertex is None: return
    postorder(vertex.left)
    postorder(vertex.right)
    print(vertex.data, end=" ")

root = node(12)
insert(root, 4)
insert(root, 18)
insert(root, 2)
insert(root, 20)
insert(root, 16)
insert(root, 9)
insert(root, 17)
insert(root, 19)
# root = node(1)
# root.insert(2)
# root.insert(3)
# root.insert(4)
# root.insert(5)
# root.insert(6)

print("\ninorder:")
inorder(root)
print("\npreorder:")
preorder(root)
print("\npostorder:")
postorder(root)
print("\npre special")
