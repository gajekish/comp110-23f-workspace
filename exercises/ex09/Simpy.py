"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "73066291"


class Simpy:
    """Creating a Simpy class with a values attribute."""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, input_list: list[float]) -> None:
        """Constructor."""
        self.values = input_list
    
    def __str__(self) -> str:
        """Formats string outputs."""
        output: str = f"Simpy({self.values})"
        return output
    
    def fill(self, fill_value: float, num_values: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = []
        for i in range(0, num_values):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of values."""
        assert step != 0.0
        self.values = []
        if (start < stop):
            while (start < stop):
                self.values.append(start)
                start += step
        else:
            while (start > stop):
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Sums all items in the values attribute."""
        return sum(self.values)
    
    def __add__(self, element: Union[float, Simpy]) -> Simpy:
        """Addition operator overload."""
        if (type(element) is Simpy):
            assert len(self.values) == len(element.values)
            new_simpy: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                new_simpy.values.append(self.values[i] + element.values[i])
        else:
            new_simpy: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                new_simpy.values.append(self.values[i] + element)
        return new_simpy
    
    def __pow__(self, element: Union[float, Simpy]) -> Simpy:
        """Power operator overload."""
        if (type(element) is Simpy):
            assert len(self.values) == len(element.values)
            new_simpy: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                new_simpy.values.append(self.values[i] ** element.values[i])
        else:
            new_simpy: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                new_simpy.values.append(self.values[i] ** element)
        return new_simpy
    
    def __eq__(self, element: Union[float, Simpy]) -> list[bool]:
        """Equality (==) operator overload."""
        if (type(element) is Simpy):
            assert len(self.values) == len(element.values)
            new_list: list = []
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] == element.values[i])
        else:
            new_list: list = []
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] == element)
        return new_list
    
    def __gt__(self, element: Union[float, Simpy]) -> list[bool]:
        """Greater than (>) operator overload."""
        if (type(element) is Simpy):
            assert len(self.values) == len(element.values)
            new_list: list = []
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] > element.values[i])
        else:
            new_list: list = []
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] > element)
        return new_list
    
    def __getitem__(self, index: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription ([]) operator overload."""
        if (type(index) is int):
            return self.values[index]
        else:
            assert len(self.values) == len(index)
            new_simpy: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                if (index[i] is True):
                    new_simpy.values.append(self.values[i])
            return new_simpy