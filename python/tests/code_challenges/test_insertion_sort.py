from code_challenges.sorting.insertion.insertion_sort import insertion_sort


def test_insertion_sort_reversed():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_insertion_sort_few_uniques():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_insertion_sort_nearly_sorted():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_insertion_sort_all_same():
    actual = insertion_sort([5, 5, 5, 5, 5, 5, 5, 5])
    expected = [5, 5, 5, 5, 5, 5, 5, 5]
    assert actual == expected


def test_insertion_sort_empty():
    actual = insertion_sort([])
    expected = []
    assert actual == expected
