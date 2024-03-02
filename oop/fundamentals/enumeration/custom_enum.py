""" Customize Python enum classes """
# Python enumerations are classes. 
# It means that you can add methods to them, or implement the dunder methods to customize their behaviors.

from enum import Enum
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3
    
print(PaymentStatus.PENDING, type(PaymentStatus.PENDING))

# To customize how the PaymentStatus member’s is represented in the string, 
# you can implement the __str__ method. For example:
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETE = 2
    REFUND = 3
    
    def __str__(self):
        return str(self.PENDING.value)

status = PaymentStatus.PENDING
print(status)
print(PaymentStatus.PENDING)

""" Implementing __eq__ method """
# The following attempts to compare a member of the PaymentStatus enum class with an integer:

class PaymentStatus(Enum):
    PENDING = 1
    COMPLETE = 2
    REFUND = 3
    
    def __eq__(self, other):
        return self.value is other

print(PaymentStatus.PENDING == 1) # False without implementation of __eq__ method
print(1 == PaymentStatus.PENDING)

""" Implementing __lt__ method """
# Suppose that you want the members of the PaymentStatus to follow have a sort order based on their value. 
# And you also want to compare them with an integer.
# To do that, you can implement the __lt__ method and use the @total_ordering decorator from 
# the functools module:

from enum import Enum
from functools import total_ordering

@total_ordering
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETE = 2
    REFUND = 3
    
    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other):
        return self.value is other
    
    def __lt__(self, other):
        return self.value < other
    
status = PaymentStatus.PENDING
print(status)
print(PaymentStatus.PENDING == 1)
print(PaymentStatus.PENDING < 2) # False, <, >, <=, >= is not supported by Enum, for that @total_ordering

""" Implementing the __bool__ method """
# By default, all members of an enumeration are truthy. For example:

class PaymentStatus(Enum):
    PENDING = 1
    COMPLETE = 2
    REFUND = 3
    
for status in PaymentStatus:
    print(status, bool(status))
    
# To customize this behavior, you need to implement the __bool__ method. 
# Suppose you want the COMPLETED and REFUNDED members to be True while the PENDING to be False.

from enum import Enum, unique

@unique
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETE = 2
    REFUND = 3
    
    def __bool__(self):
        return self is not self.PENDING

for member in PaymentStatus:
    print(member, bool(member))
    
""" Extend Python enum classes """
# Python doesn’t allow you to extend an enum class unless it has no member. 
# However, this is not a limitation. 
# Because you can define a base class that has methods but no member and then extend this base class.

from enum import Enum
from functools import total_ordering

@total_ordering
class OrderedEnum(Enum):
    def __lt__(self, other):
        return self.value <= other

class ApprovalStatus(OrderedEnum):
    PENDING = 1
    PROGRESS = 2
    APPROVED = 3
    
print(ApprovalStatus.PROGRESS > 2)

""" Summary """
# Implement dunder methods to customize the behavior of Python enum classes.
# Define an emum class with no members and methods and extends this base class.