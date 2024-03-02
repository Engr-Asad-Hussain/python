""" Introduction to the Python __new__ method """
# When you create an instance of a class, Python first calls the __new__() method to create the 
# object and then calls the __init__() method to initialize the object’s attributes.

# The first argument of the __new__ method is the class of the new object that you want to create.
# The *args and **kwargs parameters must match the parameters of the __init__() of the class. 
# However, the __new__() method does use them.
# The __new__() method should return a new object of the class. But it doesn’t have to.
# When you define a new class, that class implicitly inherits from the object class. 
# It means that you can override the __new__ static method and do something before and after 
# creating a new instance of the class.
# To create the object of a class, you call the super().__new__() method.

""" Python __new__ method example """

class Person:
    def __init__(self, name):
        self.name = name

person = Person('Asad Hussain')
# In Python, a class is callable. When you call the class to create a new object:
# Python will call the __new__() and __init__() methods. It’s equivalent to the following method calls:

person = object.__new__(Person, 'Asad Hussain')
print(person.__dict__)
person.__init__('Asad Hussain')
print(person.__dict__)

# The following illustrates the sequence which Python calls the __new__ and __init__ method when 
# you create a new object by calling the class:
class Person:
    def __new__(cls, name):
        print(f'creating a new {cls.__name__} object ...')
        obj = object.__new__(cls)
        return obj

    def __init__(self, name):
        print(f'Initiallizing the {self.__class__} object')
        self.name = name

person = Person('Asad Hussain')
# creating a new Person object ...
# Initiallizing the <class '__main__.Person'> object

""" When using the __new__ method """

class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 2)

x = SquareNumber(2)
print(x)

# In this example, the __new__() method of the SquareNumber class accepts an integer and returns 
# the square number. x is an instance of the SquareNumber class and also an instance of the int 
# built-in type:

# Note that you cannot do this by using the __init__() method because the __init__() method of the 
# built-in int takes no argument. The following code will result in an error:
class SquareNumber:
    def __init__(self, value):
        super().__init__(value ** 2)

# x = SquareNumber(3) # TypeError

# In practice, you use the __new__() method when you want to tweak the object at the instantiated time.

class Person:
    def __new__(cls, first_name: str, last_name: str):
        obj = super().__new__(cls)
        obj.first_name = first_name
        obj.last_name = last_name
        obj.full_name = f'{first_name} {last_name}'
        return obj

person = Person('Asad', 'Hussain')
print(person.__dict__)
print(Person.__dict__)

# Typically, when you override the __new__() method, you don’t need to define the __init__() method 
# because everything you can do in the __init__() method, you can do it in the __new__() method.

""" Summary """
# The __new__() is a static method of the object class.
# When you create a new object by calling the class, Python calls the __new__() method to create 
# the object first and then calls the __init__() method to initialize the object’s attributes.
# Override the __new__() method if you want to tweak the object at creation time.