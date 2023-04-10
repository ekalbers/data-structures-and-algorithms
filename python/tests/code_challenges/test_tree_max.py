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

@pytest.mark.skip('TODO')
def test_max_happy():
    tree = BinaryTree()
    tree.root = Node()


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
