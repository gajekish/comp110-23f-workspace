"""EX04 - List Utilities."""
__author__ = "730662291"


def all(integers: list[int], number: int) -> bool:
    """Returns True if all of the integers in the given list are equal to a given number and vice versa."""
    count: int = 0
    if (len(integers) == 0):
        return False
    while (len(integers) > count):
        if (integers[count] == number):
            count += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the largest integer in the given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    count: int = 1
    while (len(input) > count):
        if (input[count] > max):
            max = input[count]
        count += 1 
    return max


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Returns True if all of the elements in both of the given lists are the same and vice versa."""
    count: int = 0
    if (len(lst1) != len(lst2)):
        return False
    while (len(lst1) > count):
        if (lst1[count] == lst2[count]):
            count += 1
        else:
            return False
    return True