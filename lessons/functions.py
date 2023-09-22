"""Example Functions"""

def my_max(number1: int, number2: int):
    """Returns the maximum value out of two numbers"""
    if (number1 >= number2):
        return number1
    else: #number 1 < number 2
        return number2
    
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,10)
print(max_number)
print(other_max_number)