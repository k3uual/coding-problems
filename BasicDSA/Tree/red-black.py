class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.parent = None
        self.right = None
        self.left = None

    def grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def sibling(self, node):
        if node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left

    def uncle(self, node):
        if node.parent is None:
            return None
        return node.parent.sibling()

class red_black:
    def __init__(self):
        self.root = None

    def recolor(self, new_node):
        uncle = new_node.uncle()
        uncle.color = 'black'
        new_node.parent.color = 'black'
        new_node.grandparent().color = 'red'
        new_node = new_node.grandparent()

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        
        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        
        left_child.parent = node.parent
        
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child 
        
        left_child.right = node
        node.parent = left_child

    def insert_fix(self, new_node):
        while new_node and new_node.parent.color == 'red':
            if new_node.uncle() and new_node.uncle().color == 'red':
                self.recolor(new_node)
            else:
                if new_node.grandparent() and new_node.parent == new_node.grandparent().left:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.color = 'black'
                    new_node.grandparent().color = 'red'
                    self.rotate_right(new_node.grandparent())
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.color = 'black'
                    new_node.grandparent().color = 'red'
                    self.rotate_left(new_node.grandparent())
        self.root.color = 'black'

    def insert(self, value):
        new_node = RBNode(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                if new_node.value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        break
                    else: curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        break
                    else: curr_node = curr_node.right
        self.insert_fix(new_node)