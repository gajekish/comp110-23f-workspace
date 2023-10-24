"""Practice with Dictionaries"""

#Constructing a Dictionary
ice_cream: dict[str, int] = {"Chocolate": 12, "Vanilla": 8, "Strawberry": 5}
print(ice_cream)

#Adding a key-value pair to a dictionary
ice_cream["Mint"] = 3
print(ice_cream)

#Removing a key-value pair from a dictionary
ice_cream.pop("Mint")
print(ice_cream)

#Accessing a value
print(f"There are {ice_cream['Chocolate']} orders of chocolate")

#Adjusting a value
ice_cream["Vanilla"] += 2
#Same as ice_cream["Vanilla"] = 10
print(ice_cream)

#Getting the length
print(f"The number of key value pairs is: {len(ice_cream)}")

#Checking if a value is in a dictionary 
if ("Mint" in ice_cream):
    print(f"There are {ice_cream['Mint']} orders of mint")
else:
    print("There are no orders of mint")

#Loop through and print out every flavor and its number of orders
for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders")