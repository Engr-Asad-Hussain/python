""" Introduction to class attributes """

from asyncore import read


class Circle:
    def __init__(self, radius) -> None:
        self.pi = 3.141
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius

# The Circle class has two instance attributes pi and radius.
# In other words, they belong to a specific instance of the Circle class.

# The class attributes don’t associate with any specific instance of the class. But they’re shared by all instances of the class.

class Circle:
    pi = 3.141
    
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius

""" How Python class attributes work """
# When you access an attribute via an instance of the class, Python searches for the 
# attribute in the instance attribute list. 
# If the instance attribute list doesn’t have that attribute, Python continues looking up 
# the attribute in the class attribute list. 
# Python returns the value of the attribute as long as it finds the attribute in the instance 
# attribute list or class attribute list.

# However, if you access an attribute, Python directly searches for the attribute in the 
# class attribute list.

""" When to use Python class attributes """
# Storing class constants
# Tracking data across of all instances
# Defining default values

""" Summary """
# A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method.
# Use class_name.class_attribute or object_name.class_attribute to access the value of the class_attribute.
# Use class attributes for storing class contants, track data across all instances, and setting default values for all instances of the class.