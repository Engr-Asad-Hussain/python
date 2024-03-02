""" Introduction to the enum aliases """
# By definition, the enumeration member values are unique. 
# However, you can create different member names with the same values.

from enum import Enum
class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    CRISMON = 1
    
# In this example, the Color enumeration has the RED and CRIMSON members with the same value 1.
# When you define multiple members in an enumeration with the same values, Python does not create 
# different members but aliases.
# In this example, the RED is the main member while the CRIMSON member is the aliases of the RED member.

# When you look up a member by value, you’ll always get the main member, not aliases. 
# For example, the following statement returns the RED member:
print(Color(1))

# When you iterate the members of an enumeration with aliases, you’ll get only the main members, 
# not the aliases. For example:
for color in Color:
    print('color', color)
    
# To get all the members including aliases, you need to use the __member__ property of the enumeration class
print(Color.__members__)

""" When to use enum aliases """
class Color(Enum):
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1
    
    SUCCESS = 2
    OK = 2
    FULFILLED = 2
    
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3
    
for color in Color:
    print(color)
    
""" @enum.unique decorator """
# To define an enumeration with no aliases, you can carefully use unique values for the members. For example:

class Days(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'
    
# But you can accidentally use the same values for two members:
# To ensure an enumeration has no alias, you can use the @enum.unique decorator from the enum module.
# When you decorate an enumeration with the @enum.unique decorator, Python will throw an exception 
# if the enumeration has aliases.
from enum import Enum, unique

@unique
class Days(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'
    
""" Summary """
# When an enumeration has different members with the same values, the first member is the main 
# member while others are aliases of the main member.
# Use the @enum.unique decorator from the enum module to enforce the uniqueness of the values of 
# the members.