"""File to define Fish class."""


class Fish:
    """Creating a River Class with an age attribute."""
    age: str

    def __init__(self) -> None:
        """Constructor."""
        self.age = 0
    
    def one_day(self) -> None:
        """Increases the value of age by 1."""
        self.age += 1