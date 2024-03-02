""" Introduction to the Python __str__ method """

# Let’s start with the Person class:
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

# The Person class has three instance attributes including first_name, last_name, and age.
# The following creates a new instance of the Person class and display it:
person = Person('Asad', 'Hussain', 20)
print(person)

# When you use the print() function to display the instance of the Person class, the print() 
# function shows the memory address of that instance.

# Sometimes, it’s useful to have a string representation of an instance of a class. 
# To customize the string representation of a class instance, the class needs to implement 
# the __str__ magic method.

# Internally, Python will call the __str__ method automatically when an instance calls 
# the str() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person({self.name}, {self.age})'

# And when you use the print() function to print out an instance of the Person class, 
# Python calls the __str__ method defined in the Person class. For example:
person = Person('Asad Hussain', 20)
print(person)

""" Summary """
# Implement the __str__ method to customize the string representation of an instance of a class.