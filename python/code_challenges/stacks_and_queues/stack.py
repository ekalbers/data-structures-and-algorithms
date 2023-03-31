from ..linked_list.linked_list import Node


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        top = self.top
        self.top = Node(value, top)

    def pop(self):
        if self.top:
            stack_top = self.top
            self.top = stack_top.next
            return stack_top.value
        else:
            raise InvalidOperationError('Method not allowed on empty collection')

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError('Method not allowed on empty collection')

    def is_empty(self):
        if self.top:
            return False
        return True

    def some_method(self):
        # method body here
        pass


class InvalidOperationError(Exception):
    print(Exception)
