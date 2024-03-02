""" Introduction to encapsulation in Python """
# Encapsulation is one of the four fundamental concepts in object-oriented programming 
# including abstraction, encapsulation, inheritance, and polymorphism.

# Encapsulation is the packing of data and functions that work on that data within a 
# single object. By doing so, you can hide the internal state of the object from the outside. 
# This is known as information hiding.

# A class is an example of encapsulation. 
# A class bundles data and methods into a single unit. 
# And a class provides the access to its attributes via methods.

from locale import currency


class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current 

    def reset(self):
        self.current = 0

# The Counter class has one instance attribute called current which defaults to zero. 
# And it has three methods:

counter = Counter() # 0
counter.increment() # 1
counter.increment() # 2
counter.increment() # 3
print(counter.value()) # 3

# It works perfectly fine but has one issue.
# From the outside of the Counter class, you still can access the current attribute and 
# change it to whatever you want. For example:

counter.current = -999
print(counter.value()) # -999

# So how do you prevent the current attribute from modifying outside of the Counter class?
# That’s why private attributes come into play.

""" Private attributes """
# Private attributes can be only accessible from the methods of the class. 
# In other words, they cannot be accessible from outside of the class.

class Counter:
    # By doing this, you cannot access the __attribute directly from the outside of a class like:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current 

    def reset(self):
        self.__current = 0

counter = Counter() # 0
counter.increment() # 1
counter.__current = -999
print(counter.value()) # 1
counter.increment() # 2
print(counter.value()) # 2
print(counter.__current) # -999

# However, you can access the __current attribute as _Counter___current like this:
print(counter._Counter__current) # 2


""" Summary """
# Encapsulation is the packing of data and methods into a class so that you can hide the information and restrict access from outside.
# Prefix an attribute with a single underscore (_) to make it private by convention.
# Prefix an attribute with double underscores (__) to use the name mangling.