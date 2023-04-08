from code_challenges.trees.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """
    def add(self, value, root=None):
        if not root and self.root:
            root = self.root
        elif not self.root:
            self.root = Node(value)
            return
        if root.value < value:
            if root.right:
                self.add(value, root.right)
            else:
                root.right = Node(value)
        else:
            if root.left:
                self.add(value, root.left)
            else:
                root.left = Node(value)

    def contains(self, value, root=None):
        if not root:
            root = self.root
        if value == root.value:
            return True
        else:
            if root.right:
                if self.contains(value, root.right):
                    return True
            if root.left:
                if self.contains(value, root.left):
                    return True
        return False


