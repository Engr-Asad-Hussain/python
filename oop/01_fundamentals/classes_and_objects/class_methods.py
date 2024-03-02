""" Introduction to Python class methods """

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def introduce(self):
        return f'Hey, I am {self.get_full_name()} and I am {self.age} years old!'

# Suppose that you want to add a method that creates an anonymous person to the Person class.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def introduce(self):
        return f'Hey, I am {self.get_full_name()} and I am {self.age} years old!'
    
    def anonymous(self):
        return Person('Asad', 'Hussain', 20)

# However, to invoke the create_anonymous() method, you need to create an instance, 
# which doesn’t make sense in this case.
# This is why Python class methods come into play.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def introduce(self):
        return f'Hey, I am {self.get_full_name()} and I am {self.age} years old!'
    
    @classmethod
    def anonymous(cls):
        return Person('Asad', 'Hussain', 20)

# The anonymous() method cannot access instance attributes. But it can access class attributes via the cls variable.

""" Calling Python class methods """

anonymous = Person.anonymous()
print(anonymous.introduce())

""" Summary """
# Python class methods aren’t bound to any specific instance, but classes.
# Use @classmethod decorator to change an instance method to a class method. Also, pass the cls as the first parameter to the class method.
# Use class methods for factory methods.