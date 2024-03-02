""" Introduction to the Python __init__() method """
# When you create a new object of a class, 
# Python automatically calls the __init__() method to initialize the object’s attributes.

# Unlike regular methods, the __init__() method has two underscores (__) on each side. 
# Therefore, the __init__() is often called dunder init. 
# The name comes abbreviation of the double underscores init.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Asad Hussain', 20)
print(person.name, person.age)

""" The __init__ method with default parameters """

class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

person = Person('Asad Hussain')
print(person.name, person.age)

student = Person('Asad Hussain', 40)
print(student.name, student.age)

""" Summary """
# Use the __init__() method to initialize the object’s attributes.
# The __init__() doesn’t create an object but is automatically called after the object is created.
