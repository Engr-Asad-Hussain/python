""" Introduction to the Python property decorator """

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        
    def get_age(self):
        return self._age

    age = property(fget=get_age)

person = Person('Asad Hussain', 20)
print(person.name, person.age)

# So to get the age of a Person object, you can use either the age property or the get_age() 
# method. This creates an unnecessary redundancy.

# To avoid this redundancy, you can rename the get_age() method to the age() method like this:

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def age(self):
        return self._age

    age = property(fget=age)

person = Person('Asad', 20)
print(person.age)

# The property() accepts a callable (age) and returns a callable. Therefore, it is a decorator. 
# Therefore, you can use the @property decorator to decorate the age() method as follows:

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age

person = Person('Asad', 23)
print(person.age)

""" Setter decorators """

class Person:
    print('1')
    def __init__(self, name, age):
        print('2')
        self.name = name
        self.age = age

    @property
    def age(self):
        print('3')
        return self._age

    @age.setter
    def age(self, value):
        print('4')
        if value < 0: raise ValueError('Age cannot be negative')
        self._age = value

    # age = age.setter(set_age)


person = Person('Asad', 25)
print(person.name, person.age)
person.age = 20
print(person.name, person.age)

# The following example uses the @property decorators to create the name and age properties 
# in the Person class:
class Person:
    def __init__(self, name=None, age=None):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0: raise ValueError('Age cannot be negative')
        self._age = value

person = Person()
print(person.__dict__)

print(person.name)
print(person.age)

person.name = '   Asad Hussain   '
person.age = 20
print(person.__dict__)

""" Summary """
# Use the @property decorator to create a property for a class.