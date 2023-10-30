"""Test my zip function."""
__author__ = "730662291"

from lessons.zip import zip


def test_lists_of_different_lengths() -> None:
    """Testing for if the lists are different lengths."""
    test_list: list[str] = ["a", "b", "c"]
    test_list2: list[int] = [1, 2, 3, 4]
    assert zip(test_list, test_list2) == {}


def test_lists_of_same_lengths() -> None:
    """Testing for if the lists are same lengths."""
    test_list: list[str] = ["a", "b", "c", "d"]
    test_list2: list[int] = [1, 2, 3, 4]
    assert zip(test_list, test_list2) == {"a": 1, "b": 2, "c": 3, "d": 4}    


def test_list_with_negative_numbers() -> None:
    """Testing for if one list has negative integers."""
    test_list: list[str] = ["a", "b", "c", "d"]
    test_list2: list[int] = [-1, 2, 3, -4]
    assert zip(test_list, test_list2) == {"a": -1, "b": 2, "c": 3, "d": -4}   