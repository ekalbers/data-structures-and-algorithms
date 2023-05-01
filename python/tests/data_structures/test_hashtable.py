import pytest
from code_challenges.hashtables.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_null():
    hashtable = Hashtable()
    actual = hashtable.get('apple')
    expected = None
    assert actual == expected


def test_keys():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.keys()
    expected = ['ahmad', 'listen', 'silent']

    assert actual == expected


def test_collision():
    hashtable = Hashtable(1024)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    assert hashtable.hash('silent') == hashtable.hash('silent')
    assert hashtable.get('silent')
    assert hashtable.get('listen') == 'to me'


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["ahmad", 30]], [["listen", "to me"], ["silent", True]]]

    assert actual == expected
