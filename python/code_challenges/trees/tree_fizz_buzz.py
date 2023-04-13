from code_challenges.stacks_and_queues.queue import Queue


def fizz_buzz_tree(tree):
    new_tree = KaryTree()
    if not tree.root:
        return new_tree
    queue = Queue()
    queue.enqueue(tree.root)
    new_tree.root = Node(str(tree.root.value))
    new_queue = Queue()
    new_queue.enqueue(new_tree.root)
    while not queue.is_empty():
        current = queue.dequeue()
        new_current = new_queue.dequeue()

        children = []
        for child in current.children:
            queue.enqueue(child)
            new_child = Node(str(child.value))
            new_queue.enqueue(new_child)
            children.append(new_child)

        new_current.children = children

        if current.value % 3 == 0 and current.value % 5 == 0:
            new_current.value = 'FizzBuzz'
        elif current.value % 3 == 0:
            new_current.value = 'Fizz'
        elif current.value % 5 == 0:
            new_current.value = 'Buzz'

    return new_tree


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        q = Queue()
        if self.root:
            q.enqueue(self.root)
        lst = []
        while not q.is_empty():
            n = q.dequeue()
            lst.append(n.value)
            for x in n.children:
                q.enqueue(x)
        return lst


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
