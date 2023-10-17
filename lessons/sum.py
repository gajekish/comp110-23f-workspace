"""Summing the elements of a list using different loops."""
__author__ = "730662291"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of vals using a while loop."""
    idx: int = 0
    sum: float = 0
    while (idx < len(vals)):
        sum += vals[idx]
        idx += 1
    return sum 


def f_sum(vals: list[float]) -> float:
    """Returns the sum of vals using a for loop."""
    sum: float = 0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of vals using a for in range() loop."""
    sum: float = 0
    for num in range(len(vals)):
        sum += vals[num]
    return sum