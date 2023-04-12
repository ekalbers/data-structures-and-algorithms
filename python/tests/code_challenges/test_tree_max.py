import pytest
from code_challenges.trees.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


# @pytest.mark.skip('TODO')
def test_max_happy():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(5)
    tree.root.right = Node(50)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(9)
    tree.root.right.left = Node(11)
    tree.root.right.right = Node(24)


def test_max_break():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected


def test_max_edge():
    tree = BinaryTree()
    tree.root = Node(10)
    actual = tree.find_maximum_value()
    expected = 10
    assert actual == expected
