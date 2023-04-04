from code_challenges.linked_list.linked_list import Node


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.helper_stack = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        value = self.stack.peek()
        if value.next:
            value = self.stack.pop()
            self.helper_stack.push_two(value)
            front = self.dequeue()
            self.stack.push_two(self.helper_stack.pop())
        elif not self.helper_stack.is_empty:
            front = self.stack.pop().value
            self.stack.push_two(self.helper_stack.pop())
        else:
            front = self.stack.pop().value
        return front


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        top = self.top
        self.top = Node(value, top)

    def push_two(self, value):
        top = self.top
        value.set_next(top)
        self.top = value

    def pop(self):
        if self.top:
            stack_top = self.top
            self.top = stack_top.next
            return stack_top
        else:
            raise InvalidOperationError('Method not allowed on empty collection')

    def peek(self):
        if self.top:
            return self.top
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




