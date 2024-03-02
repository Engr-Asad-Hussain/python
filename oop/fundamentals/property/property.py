""" Introduction to class properties """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person('{self.name}', '{self.age}')"


ali = Person('Ali', 20)

# Since age is the instance attribute of the Person class, you can assign it a new 
# value like this:
ali.age = 21
print(ali.age)

# The following assignment is also technically valid:
ali.age = -1
print(ali)

# To ensure that the age is not zero or negative, you use the if statement to add a check as follows:
# ...

""" Getter and setter """
# The getter and setter methods provide an interface for accessing an instance attribute:

# In our example, you can make the age attribute private (by convention) and define a getter 
# and a setter to manipulate the age attribute.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age < 0: raise ValueError('Age cannot be negative')
        self._age = age

    def get_age(self):
        return self._age

    def __str__(self):
        return f"Person('{self.name}', '{self._age}')"

john = Person('Asad Hussain', 20)
print(john)

jane = Person('Jane', 10)
print(jane)
# jane.set_age(-1)

# This code works just fine. But it has a backward compatibility issue.
# Suppose you released the Person class for a while and other developers have been already 
# using it. And now you add the getter and setter, all the code that uses the Person won’t work 
# anymore.

# To define a getter and setter method while achieving backward compatibility, you can use the 
# property() class.

""" The Python property class """

# In the Person class, we create a new property object by calling the property() and assign 
# the property object to the age attribute. 
# Note that the age is a class attribute, not an instance attribute.
from pprint import pprint

class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age < 0: raise ValueError('Age cannot be a negative number')
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)

pprint(Person.age)
person = Person('Asad', 20)
pprint(person.__dict__)
person.age = 22
pprint(person.age)

""" Summary """
# Use the Python property() class to define a property for a class.

# Similarly, when you read from the age property object, Python will execute the function 
# assigned to the fget argument, which is the get_age() method.