""" What is a mixin in Python """
# A mixin is a class that provides method implementations for reuse by multiple related child classes. 
# However, the inheritance is not implying an is-a relationship.

# A mixin doesn’t define a new type. Therefore, it is not intended for direction instantiation.
# A mixin bundles a set of methods for reuse. Each mixin should have a single specific behavior, 
# implementing closely related methods.
# Typically, a child class uses multiple inheritance to combine the mixin classes with a parent class.
# Since Python doesn’t define a formal way to define mixin classes, it’s a good practice to name mixin 
# classes with the suffix Mixin.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents

emp = Employee(
    name='Asad Hussain',
    skills=['git', 'GitHub', 'Python', 'MySQL', 'AWS'],
    dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']}
)

# Suppose you want to convert the Employee object to a dictionary. 
# To do that, you can add a new method to the Employee class, which converts the object to a dictionary.
# However, you may want to convert objects of other classes to dictionaries. 
# To make the code reusable, you can define a mixin class called DictMixin like the following:
class DictMixin:
    def to_dict(self):
        """ Converts objects into dict """
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes: dict) -> dict:
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)
        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class Employee(DictMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents

emp = Employee(
    name='John',
    skills=['Python Programming', 'Project Management'],
    dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']}
)
from pprint import pprint
pprint(emp.to_dict())
pprint(emp.__dict__)

""" Summary """
# A mixin class provides method implementions for resuse by multiple related subclasses.