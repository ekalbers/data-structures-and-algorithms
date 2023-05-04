import pytest
from code_challenges.hashtables.hashtable import Hashtable
from code_challenges.hashtables.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_hashtable():
    synonyms = Hashtable()
    antonyms = Hashtable()

    synonyms.set('diligent', 'employed')
    synonyms.set('fond', 'enamored')
    synonyms.set('guide', 'usher')
    synonyms.set('outfit', 'garb')
    synonyms.set('wrath', 'anger')

    antonyms.set('diligent', 'idle')
    antonyms.set('fond', 'averse')
    antonyms.set('guide', 'follow')
    antonyms.set('flow', 'jam')
    antonyms.set('wrath', 'delight')

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["wrath", "anger", "delight"],
        ["outfit", "garb", None],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_hashtable_empty():
    synonyms = Hashtable()
    antonyms = Hashtable()

    expected = []

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_no_overlap():
    synonyms = Hashtable()
    antonyms = Hashtable()

    synonyms.set('diligent', 'employed')
    synonyms.set('fond', 'enamored')
    synonyms.set('guide', 'usher')
    synonyms.set('outfit', 'garb')
    synonyms.set('wrath', 'anger')

    expected = [
        ["diligent", "employed", None],
        ["fond", "enamored", None],
        ["guide", "usher", None],
        ["wrath", "anger", None],
        ["outfit", "garb", None],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
