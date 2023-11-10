"""File to define Bear class."""


class Bear:
    """Creating a River Class with age and hunger_score attributes."""
    age: str
    hunger_score: str

    def __init__(self) -> None:
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self) -> None:
        """Increases the value of age by 1 and decreases the hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increases the hunger_score by 1 per num_fish."""
        self.hunger_score += num_fish