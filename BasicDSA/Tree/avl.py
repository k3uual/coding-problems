class node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = 1

def height(root):
    if not root:
        return 0
    return root.height

def check_bal(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)

def right_rot(x):
    y = x.left
    t = y.right
    
    y.right = x
    x.left = t
    
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def left_rot(x):
    y = x.right
    t = y.left
    
    y.left = x
    x.right = t
    
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, val):
    if root == None:
        return node(val) 
    
    if(val > root.data):
        root.right = insert(root.right, val)
    elif(val < root.data):
        root.left = insert(root.left, val)
    else:
        return root 
    
    root.height = 1 + max(height(root.left), height(root.right))

    balance = check_bal(root)

    if balance > 1 and val < root.left.data:
        return right_rot(root)
    if balance < -1 and val > root.right.data:
        return left_rot(root)
    if balance > 1 and val > root.left.data:
        root.left = left_rot(root.left)
        return right_rot(root)
    if balance < -1 and val < root.right.data:
        root.right = right_rot(root.right)
        return left_rot(root)
    
    return root

def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)

root = None

root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)
pre_order(root)