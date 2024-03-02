""" Introduction to the Python __slots__ """

# The following defines a Point2D class that has two attributes including x and y coordinates:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

point = Point2D(0, 0)
print(point)

# Each instance of the Point2D class has its own __dict__ attribute that stores the instance 
# attributes. For example:
from pprint import pprint
print(point.__dict__)

# By default, Python uses the dictionaries to manage the instance attributes. 
# The dictionary allows you to add more attributes to the instance dynamically at runtime. 
# However, it also has a certain memory overhead. 
# If the Point2D class has many objects, there will be a lot of memory overhead.

# To avoid the memory overhead, Python introduced the slots. 
# If a class only contains fixed (or predetermined) instance attributes, you can use the slots 
# to instruct Python to use a more compact data structure instead of dictionaries.

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

point = Point2D(0, 0)
# The following will cause an AttributeError error:
# By doing this, Python will not use the __dict__ for the instances of the class. 
# print(point.__dict__) # AttributeError

# Instead, you’ll see the __slots__ in the instance of the class. For example:
print(point.__slots__)

# Also, you cannot add more attributes to the instance dynamically at runtime. The following 
# will result in an error:

# point.z = 20 # AttributeError
print(point)

""" Python __slots__ and single inheritance """

# The following defines the Point2D as the base class and Point3D as a subclass that inherits 
# from the Point2D class:
class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return super().__str__()[:-1] + f', {self.z})'

point2d = Point2D(2, 3)
print(point2d)
# print(point2d.__dict__) # donot works because there is an implementation of __slots__ is base class

point3d = Point3D(2, 3, 4)
print(point3d)
print(point3d.__dict__) # it works because there is no implementation of __slots__ is subclass

""" Summary """
# Python uses dictionaries to store instance attributes of instances of a class. This allows you 
# to dynamically add more attributes to instances at runtime but also create a memory overhead.
# Define __slots__ in the class if it has predetermined instances attributes to instruct Python 
# not to use dictionaries to store instance attributes. The __slots__ optimizes the memory if 
# the class has many objects.