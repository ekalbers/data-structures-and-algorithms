from code_challenges.linked_list.linked_list import Node


class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def set(self, key, value):
        index = self.hash(key)
        current = self._buckets[index]
        new_node = Node([key, value], current)
        self._buckets[index] = new_node

    def get(self, key):
        current = self._buckets[self.hash(key)]
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

    def has(self, key):
        current = self._buckets[self.hash(key)]
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def keys(self):
        keys = []
        for key in self._buckets:
            while key:
                keys.append(key.value[0])
                key = key.next
        return keys

    def hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        total = total + len(key) * 23
        index = total % self._size
        return index


class Node(Node):
    def display(self):
        current = self
        lst = []
        while current:
            lst.append(current.value)
            current = current.next
        return lst




