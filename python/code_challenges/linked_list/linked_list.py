class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        current = self.head
        if current is None:
            return 'None'
        string = f'{{ {current.value} }}'
        current = current.next
        while current is not None:
            string += f' -> {{ {current.value} }}'
            current = current.next
        string += f' -> None'
        return string


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class TargetError:
    pass
