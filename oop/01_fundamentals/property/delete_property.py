""" Introduction to Delete Property not a Class """

# To create a property of a class, you use the @property decorator. Underhood, the @property 
# decorator uses the property class that has three methods: setter, getter, and deleter.

# By using the deleter, you can delete a property from an object. 
# Notice that the deleter() method deletes a property of an object, not a class.

from pprint import pprint
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

student = Person('Asad Hussain')
pprint(student.__dict__)
student.name = 'Aisha Habib'
pprint(student.__dict__)
pprint(Person.__dict__)

# The following uses the del keyword to delete the name property:
del student.name
pprint(student.__dict__)
pprint(Person.__dict__)

# Internally, Python will execute the deleter method that deletes the _name attribute from the person object. 
# The person.__dict__ will be empty like this:

# And if you attempt to access name property again, you’ll get an error:
print(student.name)

""" Summary """
# Use the deleter decorator to delete a property of an instance of a class.

