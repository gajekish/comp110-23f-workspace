"""File to define River class."""
__author__ = "730662291"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Creating a River Class with day, bears and fish attributes.""" 
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes Fish and Bears from the River after a certain age."""
        new_bears: list[Bear] = [] 
        new_fish: list[Fish] = []
        for bear in (self.bears):
            if (not (bear.age > 5)):
                new_bears.append(bear)
        self.bears = new_bears
        for fish in (self.fish):
            if (not (fish.age > 3)):
                new_fish.append(fish)
        self.fish = new_fish

    def remove_fish(self, amount: int) -> None:
        """Removes a given amount of Fish from the River."""
        for i in range(0, amount):
            self.fish.pop(0)

    def bears_eating(self) -> None:
        """If there are a sufficient number of fish, 3 fish are removed each time a bear eats from the River."""
        for bear in (self.bears):
            if (len(self.fish) >= 5):
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self) -> None:
        """Removes bears that starve and have a hunger_score less than 0."""
        new_bears: list[Bear] = []
        for bear in (self.bears):
            if (not (bear.hunger_score < 0)):
                new_bears.append(bear)
        self.bears = new_bears
        
    def repopulate_fish(self) -> None:
        """Adds 4 new fish to the population per each pair of fish."""
        for i in range(0, (len(self.fish) // 2) * 4):
            self.fish.append(Fish())
    
    def repopulate_bears(self) -> None:
        """Adds 1 new bear to the population per each pair of bears."""
        for i in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
    
    def view_river(self) -> None:
        """Outputs information about the day and population of River."""
        output: str = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish Population: {len(self.fish)}\n"
        output += f"Bear Population: {len(self.bears)}"
        print(output)

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None:
        """Calls one_river_day() 7 times to simulate a week."""
        for i in range(0, 7):
            self.one_river_day()