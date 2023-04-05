from code_challenges.linked_list.linked_list import Node
from code_challenges.stacks_and_queues.stack import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        node = Node(value)
        if self.front:
            if self.back:
                self.back.set_next(node)
                self.back = node
            else:
                self.back.set_next(node)
                self.back = node
        else:
            self.front = node
            self.back = node

    def dequeue(self):
        if self.front:
            return_value = self.front.value
            if self.front.next:
                self.front = self.front.next
            else:
                self.front = None
            return return_value
        else:
            raise InvalidOperationError

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        if self.front:
            return False
        return True
