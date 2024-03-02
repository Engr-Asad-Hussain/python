""" Introduction to the Python Protocol """

# Suppose you have a function that calculates the total value of a product list, 
# where each product has the name, quantity, and price attributes:
from typing import List
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

def calculate_total(items: List[Product]) -> int:
    return sum([prod.quantity * prod.price for prod in items])

items = [
    Product('Mouse', 2, 250),
    Product('Keyboard', 3, 550)
]

print(calculate_total(items))

# In this example, the calculate_total() function accepts a list of Product objects and 
# returns the total value.

# When writing this function, you may want to calculate the total of a product list. But you 
# likely want to use it for other lists such as inventory lists in the future.

# If you look closely at the calculate_total() function, it only uses the quantity and price 
# attributes.

# To make the calculate_total() more dynamic while leveraging type hints, you can use the 
# Protocol from the typing module. The Protocol class has been available since Python 3.8, 
# described in PEP 544.

from pprint import pprint
from typing import Protocol
# First, define an Item class that inherits from the Protocol with two 
# attributes: quantity and price:
class Item(Protocol):
    quantity: int
    price: float

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Second, change the calculate_total() function that accepts a list of Item objects 
# instead of a list of Product objects:
def calculate_total(items: List[Item]):
    return sum([item.quantity * item.price for item in items])

# By doing this, you can pass any list of Item objects to the calculate_total() function 
# with the condition that each item has two attributes quantity and price.
total = calculate_total([
    Product('Keyboard', 2, 800),
    Product('Mouse', 3, 250)
])
print(total)

total = calculate_total([
    Inventory('Food', 25, 150),
    Inventory('Stones', 150, 250)
])
print(total)

# In this example, the Product and Inventory class don’t need to subclass the Item 
# class but still can be used in the calculate_total() function.

# This is called duck typing in Python. In duck typing, the behaviors and properties of an 
# object determine the object type, not the explicit type of the object.

# For example, an object with the quantity and price will follow the Item protocol, 
# regardless of its explicit type.

""" Summary """
# Use Python Protocol to define implicit interfaces.

