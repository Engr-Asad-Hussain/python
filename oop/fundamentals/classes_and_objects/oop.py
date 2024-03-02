""" Defining Attributes """
class Person:
    pass

person = Person()
# classes are callable
# 'Person' is the name of a class
# 'person' is the instance of Person

""" Defining Attributes """

# Python is dynamic it means we can define class attributes dynamically at runtime.
person.name = 'Asad Hussain'
person.age  = 20

print(person.name, person.age, Person())

# To define and initialize an attribute for all instances of a class, you use the __init__ method. 
# The following defines the Person class with two instance attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# When you create a Person object, Python automatically calls the __init__ method to 
# initialize the instance attributes. 
# In the __init__ method, the self is the instance of the Person class.
person = Person('Asad Hussain', 20)
print(person.name, person.age)

""" Defining Instance Methods """

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = 20

    def greet(self):
        return f'Hey, Mr. {self.name}. Your age is found to be {self.age}'

person = Person('Asad Hussain', 20)
print(person.greet())

""" Define class attributes """

# Unlike instance attributes, class attributes are shared by all instances of the class.
# The following defines the counter class attribute in the Person class:
class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = 20

    def greet(self):
        return f'Hey, Mr. {self.name}'

print(Person.counter)

# You can also access class attributes from the instance of a class too.
person = Person('Asad Hussain', 20)
print(person.counter)

# To make the counter variable more useful, you can increase its value by one once an 
# object is created. 
# To do it, you increase the counter class attribute in the __init__ method:
class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

# The following creates two instances of the Person class and shows the value of the counter:
person1 = Person('Asad Hussain', 20)
person2 = Person('Aisha', 20)
print('counter', Person.counter)

""" Define class method """

# Like a class attribute, a class method is shared by all instances of the class. 
# The first argument of a class method is the class itself. 
# By convention, its name is cls. 
# Python automatically passes this argument to the class method. 
# Also, you use the @classmethod decorator to decorate a class method.
class Person:
    print('start class')
    counter = 0
    def __init__(self, name, age):
        print('1')
        self.name = name
        self.age = age
        print('2')

    @classmethod
    def create_anonymous(cls):
        print('3')
        return Person('Anonymous', 22)

print('4')
anonymous = Person.create_anonymous()
print('5')
print(anonymous)
print('6')
print(anonymous.name)

""" Define static method """

# A static method is not bound to a class or any instances of the class. 
# In Python, you use static methods to group logically related functions in a class. 
# To define a static method, you use the @staticmethod decorator.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9

# To call a static method, you use the ClassName.static_method_name() syntax
f = TemperatureConverter.celsius_to_fahrenheit(32)
print(f)

""" Single inheritance """

# A class can reuse another class by inheriting it. 
# When a child class inherits from a parent class, the child class can access the attributes 
# and methods of the parent class.
class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hey, Mr. {self.name}. '

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    
    # To override the greet() method in the Person class, you can define the greet() method 
    # in the Employee class as follows:
    def greet(self):
        return super().greet() + f'I will be {self.job_title} @Google'

# Inside the __init__ method of the Employee class calls the __init__method of the Person 
# class to initialize the name and age attributes. 
# The super() allows a child class to access a method of the parent class.

employee = Employee('Asad Hussain', 20, 'Software Engineer')
print(employee.name, employee.age, employee.job_title)
print(employee.greet())
