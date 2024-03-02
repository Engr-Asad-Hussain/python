""" Introduction to the Python __eq__ method """

# Suppose that you have the following Person class with three instance 
# attributes: first_name, last_name, and age
from pickle import FALSE


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# And you create two instances of the Person class:
asad = Person('Asad', 'Hussain', 20)
ashfaq = Person('Ashfaq', 'Ahmed', 20)

# In this example, the john and jane objects are not the same object. 
# And you can check it using the is operator:
print(asad is ashfaq)

# Also, when you compare john with jane using the equal operator (==), 
# you’ll get the result of False:
print(asad == ashfaq)

# Since asad and ashfaq have the same age, you want them to be equal. In other words, 
# you want the following expression to return True:

# To do it, you can implement the __eq__ dunder method in the Person class.
# Python automatically calls the __eq__ method of a class when you use the == operator to 
# compare the instances of the class. 
# By default, Python uses the is operator if you don’t provide a specific implementation 
# for the __eq__ method.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

# Now, if you compare two instances of the Person class with the same age, it returns True:
john = Person('John', 'Johnny', 20)
jane = Person('Jane', 'Johnny', 20)
print(jane == john)

# The following compares a Person object with an integer: Returns AttributeError
# print(john == 20)

# To fix this, you can modify the __eq__ method to check if the object is an instance of the 
# Person class before accessing the age attribute.
# If the other object isn’t an instance of the Person class, the __eq__ method returns False, 
# like this:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False

john = Person('John', 20)
jane = Person('Jane', 20)
print(john == 20)
print(john == jane)

""" Summary """

# Implement the Python __eq__ method to define the equality logic for comparing two objects 
# using the equal operator (==)