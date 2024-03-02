""" Introduction to the Python readonly property """

# The following example defines a class called Circle that has a radius attribute and an area() method:
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

large_circle = Circle(10)
print(large_circle.area())

# But it would be more natural that the area is a property of the Circle object, not a method. 
# To make the area() method as a property of the Circle class, you can use the @property 
# decorator as follows:
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

circle = Circle(10)
print(circle.area)

# The area is calculated from the radius attribute. 
# Therefore, it’s often called a calculated or computed property.

""" Cache calculated properties """
# Suppose you create a new circle object and access the area property many times. Each time, 
# the area needs to be recalculated, which is not efficient.
# To make it more performant, you need to recalculate the area of the circle only when 
# the radius changes. If the radius doesn’t change, you can reuse the previously calculated area.

import math
class Circular:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0: raise ValueError('Radius cannot be negative')
        if value != self._radius:
            self._radius = value
            self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius**2
        return self._area

circle = Circular(10)
print(circle.area)
print(circle.radius)
circle.radius = 15
print(circle.radius)
print(circle.area)

""" Summary """
# Define only the getter to make a property readonly
# Do use computed property to make the property of a class more natural
# Use caching computed properties to improve the performance.