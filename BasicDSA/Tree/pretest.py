# Python program for preorder traversals

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print preorder traversal
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)


# Driver code
if __name__ == '__main__':
    root = Node(12)
    root.left = Node(4)
    root.right = Node(18)
    root.left.left = Node(2)
    root.left.right = Node(9)
    root.right.right = Node(20)
    root.right.left = Node(16)
    root.right.left.right = Node(17)
    root.right.right.left = Node(19)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)