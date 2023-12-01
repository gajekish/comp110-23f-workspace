"""Dictionary related utility functions."""

__author__ = "730662291"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        # append every value under key header
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produces a column-based table with only a specified number of rows for each column."""
    result: dict[str, list[str]] = {}
    for col in table:
        new_list: list[str] = []
        for i in range(num_rows):
            value: list[str] = table[col]
            new_list.append(value[i])
        result[col] = new_list
    return result


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for col in col_names:
        result[col] = table[col]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for col1 in table1:
        result[col1] = table1[col1]
    for col2 in table2:
        if (col2 in result):
            for elem in table2[col2]:
                result[col2].append(elem)
        else:
            result[col2] = table2[col2]
    return result