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

def del_node(vertex, val):
    if not vertex:
        return vertex
    
    if val < vertex.data:
        vertex.left = del_node(vertex.left, val)
    elif val > vertex.data:
        vertex.right = del_node(vertex.right, val)
    
    else:
        if not vertex.left:
            return vertex.right
        elif not vertex.right:
            return vertex.left
        else:
            temp = vertex.right
            while(temp.left and temp):
                temp = temp.left
            vertex.data = temp.data
            vertex.right = del_node(vertex.right, temp.data)
        
    return vertex

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

# This function deletes a given key x from the
# given BST and returns the modified root of the 
# BST (if it is modified).
def delete(root, x):
  
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.data > x:
        root.left = del_node(root.left, x)
    elif root.data < x:
        root.right = del_node(root.right, x)
        
    else:
        # If root matches with the given data

        # Cases when root has 0 children or 
        # only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.data = succ.data
        root.right = del_node(root.right, succ.data)
        
    return root

root = node(int(input("set your root node: ")))
choice = 1
print("[add = add node,\nin = print inorder,\npre = print preorder,\npost = print postorder,\ndel = delete a node\nexit = to exit]")
while(choice):
    popup = "Pick a function to perform:\n"
    if choice == "help":
        popup = "[add = add node,\nin = print inorder,\npre = print preorder,\npost = print postorder,\ndel = delete a node\nexit = to exit]\nnow you can choose a function to perform: "
    choice = input(popup)
    choice = choice.strip()
    choice = choice.lower()
    match choice:
        case "help":
            pass
        case "add":
            val = int(input("enter value to insert: "))
            insert(root, val)
        case "in":
            inorder(root)
        case "pre":
            preorder(root)
        case "post":
            postorder(root)
        case "del":
            val = int(input("enter value to delete: "))
            del_node(root, val)
        case "exit":
            choice = 0
        case default:
            choice = "help"

# root = node(12)
# insert(root, 4)
# insert(root, 18)
# insert(root, 2)
# insert(root, 20)
# insert(root, 16)
# insert(root, 9)
# insert(root, 17)
# insert(root, 19)
# root = node(1)
# root.insert(2)
# root.insert(3)
# root.insert(4)
# root.insert(5)
# root.insert(6)
# delete(root, 20)
# del_node(root, 20)

# print("inorder:")
# inorder(root)
# print("\npreorder:")
# preorder(root)
# print("\npostorder:")
# postorder(root)
