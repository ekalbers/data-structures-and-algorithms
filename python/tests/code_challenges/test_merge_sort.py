from code_challenges.sorting.merge.merge_sort import merge_sort


def test_merge_sort_sample():
    actual = [8, 4, 23, 42, 16, 15]
    merge_sort(actual)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_merge_sort_reversed():
    actual = [20, 18, 12, 8, 5, -2]
    merge_sort(actual)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_merge_sort_few_uniques():
    actual = [5, 12, 7, 5, 5, 7]
    merge_sort(actual)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_merge_sort_nearly_sorted():
    actual = [2, 3, 5, 7, 13, 11]
    merge_sort(actual)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_merge_sort_all_same():
    actual = [5, 5, 5, 5, 5, 5, 5, 5]
    merge_sort(actual)
    expected = [5, 5, 5, 5, 5, 5, 5, 5]
    assert actual == expected


def test_merge_sort_empty():
    actual = []
    merge_sort(actual)
    expected = []
    assert actual == expected
