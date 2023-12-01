from __future__ import annotations

class ChristmasTreeFarm:
    """This is a Christmas Tree Farm."""

    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Constructor."""
        self.plots = []
        for i in range(plots):
            if (initial_planting > 0):
                self.plots.append(1)
                initial_planting -= 1
            else:
                self.plots.append(0)

    def plant(self, plot_index: int) -> None:
        """Uproots old trees and replaces them with new ones."""
        self.plots[plot_index] = 1
    
    def growth(self) -> None:
        """Increases the size of a planted tree."""
        for i in range(0, len(self.plots)):
            if (self.plots[i] != 0):
                self.plots[i] += 1

    def harvest(self, replant: bool) -> int:
        """Replants trees if so and harvests trees that are at least size 5."""
        count: int = 0
        for i in range(0, len(self.plots)):
            if (self.plots[i] >= 5):
                count += 1
                if (replant == True):
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0    
        return count
    
    def __add__(self, other_object: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Addition operator overload."""
        trees: int = 0
        for i in range(0, len(self.plots)):
            if (self.plots[i] > 0):
                trees += 1
        for i in range(0, len(other_object.plots)):
            if (other_object.plots[i] > 0):
                trees += 1
        return ChristmasTreeFarm(len(self.plots) + len(other_object.plots), trees) 