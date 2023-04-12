from code_challenges.stacks_and_queues.queue import Queue


def breadth_first(tree):
    q = Queue()
    if tree.root:
        q.enqueue(tree.root)
    lst = []
    while not q.is_empty():
        n = q.dequeue()
        lst.append(n.value)
        if n.left:
            q.enqueue(n.left)
        if n.right:
            q.enqueue(n.right)
    return lst
