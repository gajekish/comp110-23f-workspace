"""EX06 - Dictionary Functions."""
__author__ = "730662291"


def invert(some_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that inverts the keys and values."""
    inverted_dict: dict[str, str] = {}
    value: str = ""
    for key in some_dict:
        value = some_dict[key]
        if value in inverted_dict:
            raise KeyError("KeyError")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(some_dict: dict[str, str]) -> str:
    """Returns the string of the color that appears most frequently in the dictionary."""
    frequent_color: str = ""
    count: int = 0
    most: int = 0
    for key1 in some_dict:
        first_value = some_dict[key1]
        for key2 in some_dict:
            second_value = some_dict[key2]
            if (first_value == second_value):
                count += 1
        if (count > most):
            most = count
            frequent_color = first_value
        count = 0
    return frequent_color


def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary where each key is a value in the list and the associated value is how often the key appeared."""
    dictionary: dict[str, int] = {}
    count: int = 0
    for string in input:
        for elem in input:
            if (string == elem):
                count += 1
        dictionary[string] = count
        count = 0
    return dictionary


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary where each key is a letter and each value is a list of words starting with that letter."""
    word_list: list[str] = []
    dictionary: dict[str, list[str]] = {}
    for word in input:
        letter: str = word[0].lower()
        for elem in input:
            if (letter == elem[0].lower()):
                word_list.append(elem)
        dictionary[letter] = word_list
        word_list = []
    return dictionary


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Returns a mutated input_dict with days of the week as keys and a list of students in attendance as values."""
    student_list: list[str] = []
    for elem in input_dict:
        if (elem == day):
            value = input_dict[elem]
            value.append(student)
    if (day not in input_dict):
        student_list.append(student)
        input_dict[day] = student_list
    return input_dict