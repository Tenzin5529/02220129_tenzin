from collections import deque  # <-- required for is_complete_binary_tree

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self):
        self.root = None
        print("Created new Binary Tree")
        print("Root: None")

    # Wrapper function for height
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    # Wrapper for size
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    # Wrapper for counting leaves
    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)

    # Wrapper for full binary tree
    def is_full_binary_tree(self):
        return self._is_full_binary_tree(self.root)

    def _is_full_binary_tree(self, node):
        if node is None:
            return True
        if (node.left is None) != (node.right is None):
            return False
        return self._is_full_binary_tree(node.left) and self._is_full_binary_tree(node.right)

    # Complete binary tree check
    def is_complete_binary_tree(self):
        if not self.root:
            return True
        queue = deque([self.root])
        end = False
        while queue:
            current = queue.popleft()
            if current.left:
                if end:
                    return False
                queue.append(current.left)
            else:
                end = True
            if current.right:
                if end:
                    return False
                queue.append(current.right)
            else:
                end = True
        return True


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()

    # Manually build a full and complete tree
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("\nTree Height:", tree.height())
    print("Total Nodes:", tree.size())
    print("Leaf Nodes Count:", tree.count_leaves())
    print("Is Full Binary Tree:", tree.is_full_binary_tree())
    print("Is Complete Binary Tree:", tree.is_complete_binary_tree())
