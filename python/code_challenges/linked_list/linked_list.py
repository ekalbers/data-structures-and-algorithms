class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

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

    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.set_next(Node(value))

    def insert_before(self, before, value):
        current = self.head
        if current.value is not before:
            while current.next is not None and current.value is not before:
                if current.next.value is before:
                    current.set_next(Node(value, current.next))
                    break
                current = current.next
        else:
            self.insert(value)

    def insert_after(self, after, value):
        if self.includes(after):
            current = self.head
            while current.value is not after and current.next is not None:
                current = current.next
            current.set_next(Node(value, current.next))



class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

    def set_next(self, value):
        self.next = value


class TargetError:
    pass
