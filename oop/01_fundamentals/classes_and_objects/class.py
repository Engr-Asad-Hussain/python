""" Object """

# An object is a container that contains data and functionality.
# The data represents the object at a particular moment in time. 
# Therefore, the data of an object is called the state. 
# Python uses attributes to model the state of an object.

# The functionality represents the behaviors of an object. 
# Python uses functions to model the behaviors. 
# When a function is associated with an object, it becomes a method of the object.

# In other words, an object is a container that contains the state and methods.

""" Define a class """

# By convention, you use CamelCase names for classes in Python.
class Person:
    pass

# When printing out the person object, you’ll see its name and memory address:
# The id of an object is unique. In CPython, the id() returns the memory address of an object.
person = Person()
print(person, id(person), hex(id(person)))
print(isinstance(person, Person))

""" A class is also an object in Python """

# Everything in Python is an object, including classes.
# When you define the Person class, Python creates an object with the name Person. 
# The Person object has attributes. For example, you can find its name using the __name__ 
# attribute:
class Person:
    pass
print(Person.__name__)
print(type(Person))

# The Person class also has a behavior. For example, it can create a new instance:
person = Person()
print(person)
print(type(person))


""" Summary """
# An object is container that contains state and behavior.
# A class is a blueprint for creating objects.
# In Python, a class is also an object, which is an instance of the type.