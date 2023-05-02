import pytest
from code_challenges.hashtables.tree_intersection import tree_intersection
from code_challenges.trees.binary_tree import BinaryTree, Node
from code_challenges.stacks_and_queues.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def test_tree_intersection_none():
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 110, 120, 15, 170, 210, 360, 126, 180, 4, 501]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert sorted(actual) == sorted(expected)


def test_tree_intersection_empty():
    tree_a = BinaryTree()

    tree_b = BinaryTree()

    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert sorted(actual) == sorted(expected)


def test_tree_intersection_strings():
    tree_a = BinaryTree()
    values = ['Roger', 'Tyler', 'Diontre', 'Dominic', 'James', 'Sheldon', 'Darran', 'Dutch', 'Mandela', 'Mike', 'Ethan']
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = ['Jacob', 'James', 'Darran', 'Sheldon', 'Ethan', 'Ethan', 'Kawika', 'Reed']
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = ['Ethan', 'James', 'Darran', 'Sheldon']

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
