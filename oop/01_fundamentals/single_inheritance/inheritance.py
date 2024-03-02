""" Introduction to the Python inheritance """

# Inheritance allows a class to reuse the logic of an existing class. Suppose you have the following Person class:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hey, I am {self.name}'

student = Person('Asad Hussain')
print(student.greet())

# Now, you want to define the Employee that is similar to the Person class:
class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
    
    def greet(self):
       return f'Hey, I am {self.name}'

emp = Employee('Asad Hussain', 'Software Developer')
print(emp.greet())

# The Employee class has two attributes name and job_title. It also has the greet() method 
# that is exactly the same as the greet() method of the Person class.

# To reuse the greet() method from the Person class in the Employee class, you can create a 
# relationship between the Person and Employee classes. To do it, you use inheritance so that 
# the Employee class inherits from the Person class.

class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

# By doing this, the Employee class behaves the same as the Person class without redefining the greet() method.

# This is a single inheritance because the Employee inherits from a single class (Person). 
# Note that Python also supports multiple inheritances where a class inherits from multiple classes.
emp = Employee('Asad Hussain', 'Software Engineer')
print(emp.greet())

""" Inheritance terminology """
# The Person class is the parent class, the base class, or the super class of the Employee class. 
# And the Employee class is a child class, a derived class, or a subclass of the Person class.

""" type vs. isinstance """
person = Person('Asad Hussain')
print(type(person))

emp = Employee('Asad Hussain', 'Software Engineer')
print(type(emp))

# To check if an object is an instance of a class, you use the isinstance() method. For example:
print(isinstance(person, Person))
print(isinstance(emp, Employee))
print(isinstance(emp, Person))
print(isinstance(person, Employee))

""" issubclass """
print(issubclass(Person, Employee))

""" Summary """
# Inheritance allows a class to reuse existing attributes and methods of another class.
# The class that inherits from another class is called a child class, a subclass, or a derived class.
# The class from which other classes inherit is call a parent class, a super class, or a base class.
# Use isinstance() to check if an object is an instance of a class.
# Use issubclass() to check if a class is a subclass of another class.