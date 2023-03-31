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
        if self.includes(before):
            if self.head.value is not before:
                current = self.head
                while current.next:
                    if current.next.value is before:
                        current.set_next(Node(value, current.next))
                        break
                    current = current.next
            else:
                self.insert(value)
        else:
            raise TargetError

    def insert_after(self, after, value):
        if self.includes(after):
            current = self.head
            while current.value is not after and current.next is not None:
                current = current.next
            current.set_next(Node(value, current.next))
        else:
            raise TargetError

    def kth_from_end(self, k, current=None, length=0):
        if length == 0:
            current = self.head
        if current:
            index = length
            x = self.kth_from_end(k, current.next, length+1)
            if type(x) is int and x - index == k:
                return current.value
            else:
                return x
        else:
            if length < length - k or length - k <= 0:
                raise TargetError
            else:
                return length - 1

    @staticmethod
    def zip_lists(ll1, ll2):
        if ll1.head and ll2.head:
            LinkedList.helper_zip_lists(ll1.head, ll2.head)
        elif ll2.head:
            return ll2
        return ll1

    @staticmethod
    def helper_zip_lists(current1, current2):
        if current1:
            if current1.next and current2.next:
                current1_next = current1.next
                current2_next = current2.next
                current1.set_next(current2)
                current2.set_next(current1_next)
                LinkedList.helper_zip_lists(current1_next, current2_next)
            elif current2.next:
                current1.set_next(current2)
                current2.set_next(current2.next)
                LinkedList.helper_zip_lists(None, current2.next)
            elif current1.next and current2:
                current2.set_next(current1.next)
                current1.set_next(current2)
            else:
                current1.set_next(current2)
        elif current2:
            current2.set_next(current2.next)
            LinkedList.helper_zip_lists(None, current2.next)


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

    def set_next(self, value):
        self.next = value


class TargetError(Exception):
    print(Exception)
