""" Introduction to the Python __bool__ method """

# An object of a custom class is associated with a boolean value. 
# By default, it evaluates to True. For example
class Person:
    def __init__(self, name):
        self.name = name

print(bool(Person('Asad Hussain'))) # True

# To override this default behavior, you implement the __bool__ special method. 
# The __bool__ method must return a boolean value, True or False.
class Person:
    def __init__(self, age):
        self.age = age

    def __bool__(self):
        return self.age > 18

print(bool(Person(20))) # True
print(bool(Person(17))) # False

""" The __len__ method """
# If a custom class doesn’t have the __bool__ method, Python will look for the __len__() 
# method. If the __len__ is zero, the object is False. Otherwise, it’s True

# If a class doesn’t implement the __bool__ and __len__ methods, the objects of the 
# class will evaluate to True

class Payroll:
    def __init__(self, age):
        self.age = age

    def __len__(self):
        return self.age

print(bool(Payroll))
print(bool(Payroll(0))) # False because __len__ becomes 0

""" Summary """
# All objects of custom classes return True by default.
# Implement the __bool__ method to override the default. The __bool__ method must 
# return either True or False.
# If a class doesn’t implement the __bool__ method, Python will use the result of 
# the __len__ method. If the class doesn’t implement both methods, the objects will 
# be True by default.