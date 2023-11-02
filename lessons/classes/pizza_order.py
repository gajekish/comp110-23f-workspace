"""Instantiating a Class."""

# import the class
# from <file_name>.<module_name> import <class_name>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # CONSTRUCTOR

# accessing/setting attribtues
# my_pizza.size = "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True

print("Size Attribute: " + str(my_pizza.size))
print("Toppings Attribute: " + str(my_pizza.toppings))
print("Gluten Free Attribute: " + str(my_pizza.gluten_free))

# sals_pizza size 'Medium', 5 toppings, not GF
sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    """Function to Calculate Price of Pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += 0.75 * input_pizza.toppings
    if input_pizza.gluten_free == True:
        price += 1.00
    return price

# Calling price function
print(price(sals_pizza))
print(price(my_pizza))

# Calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)