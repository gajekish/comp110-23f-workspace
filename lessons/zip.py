"""Combining two lists into a dictionary."""
__author__ = "730662291"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Returns a dictionary with corresponding key value pairs from two lists of the same length."""
    new_dict: dict[str, int] = {}
    if len(keys) == len(values):
        index: int = 0
        while (index < len(keys)):
            new_dict[keys[index]] = values[index]
            index += 1
        return new_dict
    else:
        return new_dict