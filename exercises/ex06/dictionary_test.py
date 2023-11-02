"""EX07 - Dictionary Unit Tests."""
__author__ = "730662291"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_dictionary_for_invert() -> None:
    """Testing for a typical dictionary input."""
    test_dictionary: dict[str, str] = {"hello": "hi", "goodbye": "bye"}
    assert invert(test_dictionary) == {"hi": "hello", "bye": "goodbye"}
    

def test_dictionary_of_one_element() -> None:
    """Testing for a dictionary input that has only one key-value pair."""
    test_dictionary: dict[str, str] = {"Kishan": "Gajera"}
    assert invert(test_dictionary) == {"Gajera": "Kishan"}
    

def test_empty_dictionary_for_invert() -> None:
    """Testing for an empty dictionary input."""
    test_dictionary: dict[str, str] = {}
    assert invert(test_dictionary) == {}


def test_dictionary_for_favorite_color() -> None:
    """Testing for a typical dictionary input."""
    test_dictionary: dict[str, str] = {"Alex": "Yellow", "Tim": "Blue", "Bob": "Yellow"}
    assert favorite_color(test_dictionary) == "Yellow"


def test_dictionary_for_same_instances_of_colors() -> None:
    """Testing for a dictionary input that has a tie for the most common color."""
    test_dictionary: dict[str, str] = {"Alex": "Brown", "Tim": "Pink", "Bob": "Brown", "Kishan": "Pink"}
    assert favorite_color(test_dictionary) == "Brown"


def test_empty_dictionary_for_favorite_color() -> None:
    """Testing for an empty dictionary input."""
    test_dictionary: dict[str, str] = {}
    assert favorite_color(test_dictionary) == ""


def test_list_for_count() -> None:
    """Testing for a typical list input."""
    test_list: list[str] = ["a", "b", "c", "c", "a", "a", "b", "z"]
    assert count(test_list) == {"a": 3, "b": 2, "c": 2, "z": 1}


def test_list_of_one_element_for_count() -> None:
    """Testing for a list input with one element."""
    test_list: list[str] = ["Pasta"]
    assert count(test_list) == {"Pasta": 1}


def test_empty_list_for_count() -> None:
    """Testing for an empty list input."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_list_for_alphabetizer() -> None:
    """Testing for a typical list input."""
    test_list: list[str] = ["Kishan", "Pops", "Kevin", "Brad", "Brock", "Lucas", "Patrick", "Lone"]
    assert alphabetizer(test_list) == {'k': ['Kishan', 'Kevin'], 'p': ['Pops', 'Patrick'], 'b': ['Brad', 'Brock'], 'l': ["Lucas", "Lone"]}


def test_list_for_one_element_in_alphabetizer() -> None:
    """Testing for a list input with one element."""
    test_list: list[str] = ["mom"]
    assert alphabetizer(test_list) == {'m': ['mom']}


def test_empty_list_for_alphabetizer() -> None:
    """Testing for an empty list input."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_regular_input_for_update_attendance() -> None:
    """Testing for a typical input."""
    test_dictionary: dict[str, list[str]] = {"Monday": ["Michael", "Caleb"], "Tuesday": ["Grimsley"]}
    test_day: str = "Tuesday"
    test_student: str = "Matthew"
    assert update_attendance(test_dictionary, test_day, test_student) == {'Monday': ['Michael', 'Caleb'], 'Tuesday': ['Grimsley', 'Matthew']}


def test_empty_student_for_update_attendance() -> None:
    """Testing for when student is an empty string."""
    test_dictionary: dict[str, list[str]] = {"Monday": ["Michael", "Caleb"], "Tuesday": ["Grimsley"]}
    test_day: str = "Wednesday"
    test_student: str = ""
    assert update_attendance(test_dictionary, test_day, test_student) == {'Monday': ['Michael', 'Caleb'], 'Tuesday': ['Grimsley'], "Wednesday": ['']}


def test_empty_dictionary_for_update_attendance() -> None:
    """Testing for when the dictionary is empty."""
    test_dictionary: dict[str, list[str]] = {}
    test_day: str = "Wednesday"
    test_student: str = "Kishan"
    assert update_attendance(test_dictionary, test_day, test_student) == {"Wednesday": ['Kishan']}