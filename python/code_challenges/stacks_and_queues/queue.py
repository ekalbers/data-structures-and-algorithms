from code_challenges.linked_list.linked_list import Node
from code_challenges.stacks_and_queues.stack import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None):
        self.front = front
        self.back = None

    def enqueue(self, value):
        if self.front:
            if self.back:
                self.back = Node(value, self.back)
            else:
                self.back = Node(value, self.front)
        else:
            node = Node(value)
            self.front = node
            self.back = node

    def dequeue(self):
        if self.front:
            if not self.back:
                front = self.front
                self.front = None
            else:
                current = self.back
                last = current
                front = current
                while current.next:
                    last = current
                    front = current.next
                    current = current.next
                if last.next:
                    last.set_next(None)
                    self.front = last
                else:
                    self.front = None
            return front.value
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


    def some_method(self):
        # method body here
        pass
