""" Introduction to the Python __repr__ magic method """

# The __repr__ dunder method defines behavior when you pass an instance of a class to the 
# repr().
# The __repr__ method returns the string representation of an object. 
# Typically, the __repr__() returns a string that can be executed and yield the same value 
# as the object.
# In other words, if you pass the returned string of the object_name.__repr__() method to 
# the eval() function, you’ll get the same value as the object_name. 
# Let’s take a look at an example.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Second, create a new instance of the Person class and display its string representation:
person = Person('Asad', 'Hussain', 20)
print(repr(person))

# By default, the output contains the memory address of the person object. 
# To customize the string representation of the object, you can implement the __repr__ method like this:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', '{self.age}')"

person = Person('Asad Hussain', 40)
print(repr(person))

# When a class doesn’t implement the __str__ method and you pass an instance of that 
# class to the str(), Python returns the result of the __repr__ method because internally 
# the __str__ method calls the __repr__ method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', '{self.age}')"

    def __str__(self):
        return f'({self.name}, {self.age})'

person = Person('Asad Hussain', 20)
print(person)
print(repr(person))
# If you haven't implement __str__ method, and you do print(person), it will call __repr__ method.
# If you have implement __str__ method, and you do print(person), it will call __str__ method.
# repr(person) will call __repr__ method only.

""" __str__ vs __repr__ """
# The main difference between __str__ and __repr__ method is intended audiences.
# The __str__ method returns a string representation of an object that is human-readable 
# while the __repr__ method returns a string representation of an object that 
# is machine-readable.

""" Summary """
# Implement the __repr__ method to customize the string representation of an object 
# when repr() is called on it.
# The __str__ calls __repr__ internally by default.