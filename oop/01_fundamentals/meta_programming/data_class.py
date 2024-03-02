""" Introduction to the Python dataclass """

# Python introduced the dataclass in version 3.7 (PEP 557). The dataclass allows you to define 
# classes with less code and more functionality out of the box.

# The following defines a regular Person class with two instance attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This Person class has the __init__ method that initializes the name and age attributes.
# If you want to have a string representation of the Person object, you need to implement 
# the __str__ or __repr__ method. Also, if you want to compare two instances of the Person class by 
# an attribute, you need to implement the __eq__ method.

# However, if you use the dataclass, you’ll have all of these features (and even more) without 
# implementing these dunder methods.

# To make the Person class a data class, you follow these steps:

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# By doing this, the @dataclass decorator implicitly creates the __init__ method like this:
# def __init__(self, name: str, age: int)

per = Person('Asad Hussain', 20)
print(per)  # Person(name='Asad Hussain', age=20)

# Also, if you compare two Person‘s objects with the same attribute value, it’ll return True. For example:
p1 = Person('Asad Hussain', 20)
p2 = Person('Asad Hussain', 20)
print(p1 == p2) # True

""" Default values """

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    is_married: bool = False

per = Person('Asad Hussain', 32)
print(per)

""" Convert to a tuple or a dictionary """

from dataclasses import dataclass, astuple, asdict

@dataclass
class Person:
    name: str
    age: int
    is_married: bool = False

per = Person('Asad Hussain', 23, True)
print(astuple(per), asdict(per))
# ('Asad Hussain', 23, True) {'name': 'Asad Hussain', 'age': 23, 'is_married': True}

""" Create immutable objects """

# To create readonly objects from a dataclass, you can set the frozen argument of the dataclass decorator to True. For example:
from dataclasses import dataclass, astuple, asdict
@dataclass(frozen=True)
class Person:
    name: str
    age: int

per = Person('Asad Hussain', 20)
print(asdict(per))
per.name = 'Muhkil'
print(asdict(per))

""" Summary """
# Use the @dataclass decorator from the dataclasses module to make a class a dataclass. The 
# dataclass object implements the __eq__ and __str__ by default.
# Use the astuple() and asdict() functions to convert an object of a dataclass to a tuple and dictionary.
# Use frozen=True to define a class whose objects are immutable.
# Use __post_init__ method to initalize attributes that depends on other attributes.
# Use sort_index to specify the sort attributes of the dataclass objects.