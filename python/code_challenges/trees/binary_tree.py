class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, root=None, values=[]):
        if not root:
            root = self.root
        values.append(root.value)
        if root.left:
            self.pre_order(root.left, values)
        if root.right:
            self.pre_order(root.right, values)
        return values

    def in_order(self, root=None, values=[]):
        if not root:
            root = self.root
        if root.left:
            self.in_order(root.left, values)
        values.append(root.value)
        if root.right:
            self.in_order(root.right, values)
        return values

    def post_order(self, root=None, values=[]):
        if not root:
            root = self.root
        if root.left:
            self.post_order(root.left, values)
        if root.right:
            self.post_order(root.right, values)
        values.append(root.value)
        return values

    def some_method(self):
        # method body here
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
