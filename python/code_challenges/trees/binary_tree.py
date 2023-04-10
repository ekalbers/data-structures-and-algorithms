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

    def find_maximum_value(self, root=None, max_value=None):
        if not root:
            root = self.root
            if root:
                max_value = root.value
            else:
                return max_value
        if root.value > max_value:
            max_value = root.value
        if root.left:
            left_max = self.find_maximum_value(root.left, max_value)
            if left_max > max_value:
                max_value = left_max
        if root.right:
            right_max = self.find_maximum_value(root.right, max_value)
            if right_max > max_value:
                max_value = right_max
        return max_value


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
