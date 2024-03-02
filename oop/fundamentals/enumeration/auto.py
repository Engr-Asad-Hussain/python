""" Introduction to the enum auto() function """

from enum import Enum
class State(Enum):
    PENDING = 1
    COMPLETE = 2
    REJECT = 3

# In this example, we manually assign integer values to the members of the enumeration.
# To make it more convenient, Python 3.6 introduced the auto() helper class in the enum module, 
# which automatically generates unique values for the enumeration members.

from enum import Enum, auto
class State(Enum):
    PENDING = auto()
    COMPLETE = auto()
    REJECT = auto()

    def __str__(self):
        return f'{self.name}: {self.value}'

for state in State:
    print(state)
# By default, the auto() class generates a sequence of integer numbers starting from 1.

# By default, the _generate_next_value_() generates the next number in a sequence of integers starting 
# from one. However, Python may change this logic in the future.
# It’s possible to override the _generate_next_value_() method to add a custom logic that generates unique 
# values. 
# If so, you need to place the _generate_next_value_() method before defining all the members.
class State(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto()
    COMPLETE = auto()
    REJECT = auto()

    def __str__(self):
        return str(self.value)

for state in State:
    print(state)

""" Summary """
# Use enum auto() class to generate unique values for enumeration members.