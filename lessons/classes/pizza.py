"""Defining a Class!"""

from __future__ import annotations

class Pizza:

    # attributes
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool


    def __init__(self, inp_size: str, inp_toppings: int, inp_gluten_free: bool) -> None:
        """My Constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gluten_free
        # returns a Pizza object automatically


    def price(self) -> float:
        """Method to Calculate Price of Pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += 0.75 * self.toppings
        if self.gluten_free == True:
            price += 1.00
        return price
    

    def add_toppings(self, num_toppings: int) -> None:
        """Add toppings to existing pizza."""
        self.toppings += num_toppings

    
    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza