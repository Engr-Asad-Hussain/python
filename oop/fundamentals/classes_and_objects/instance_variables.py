""" Introduction to the Python instance variables"""
# In Python, class variables are bound to a class while instance variables are bound to 
# a specific instance of a class. 
# The instance variables are also called instance attributes.

from pprint import pprint
class HtmlDocument:
    extension = 'html'
    version = 5

pprint(HtmlDocument.__dict__)
print(HtmlDocument.extension, HtmlDocument.version)

home = HtmlDocument()
print(home.__dict__)

# The home.__dict__ stores the instance variables of the home object like the 
# HtmlDocument.__dict__ stores the class variables of the HtmlDocument class.

# Since a dictionary is mutable, you can mutate it e.g., adding a new element to 
# the dictionary.
# Python allows you to access the class variables from an instance of a class. For example:
print(home.extension, home.version)

# In this case, Python looks up the variables extension and version in home.__dict__ first. 
# If it doesn’t find them there, it’ll go up to the class and look up in the 
# HtmlDocument.__dict__.

# However, if Python can find the variables in the __dict__ of the instance, it won’t look 
# further in the __dict__ of the class.

home.version = 6
pprint(HtmlDocument.__dict__)
pprint(home.__dict__)

""" Initializing instance variables """

class HtmlDocument:
    version = 5
    extension = 'html'

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

blank = HtmlDocument('Blank', '')
pprint(blank.__dict__)

""" Summary """
# Instance variables are bound to a specific instance of a class.
# Python stores instance variables in the __dict__ attribute of the instance. Each instance has its own __dict__ attribute and the keys in this __dict__ may be different.
# When you access a variable via the instance, Python finds the variable in the __dict__ attribute of the instance. If it cannot find the variable, it goes up and look it up in the __dict__ attribute of the class.
