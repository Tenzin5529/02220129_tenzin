class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
            print("Created new Binary Tree")
            print(f"Root: {self.root.value}")
        else:
            self.root = None
            print("Created new Binary Tree")
            print("Root: None")


# --- Example Usage ---

# Create an empty binary tree
tree1 = BinaryTree()

# Create a binary tree with a root node value of 10
tree2 = BinaryTree(10)
