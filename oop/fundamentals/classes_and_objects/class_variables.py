""" Introduction to the Python class variables """

# Everything in Python is an object including a class. 
# In other words, a class is an object in Python.
# When you define a class using the class keyword, Python creates an object with the name 
# the same as the class’s name. For example:

from tabnanny import verbose


class HtmlDocument:
    pass

print(HtmlDocument)
print(HtmlDocument.__name__)
print(type(HtmlDocument))
print(isinstance(HtmlDocument, type))

# Class variables are bound to the class. They’re shared by all instances of that class.
class HtmlDocument:
    extension = 'html'
    version = 5

# Both extension and version are the class variables of the HtmlDocument class. 
# They’re bound to the HtmlDocument class.

print(HtmlDocument.extension, HtmlDocument.version)

# If you access a class variable that doesn’t exist, you’ll get an AttributeError exception. 
# For example:
# print(HtmlDocument.media_type)

# Another way to get the value of a class variable is to use the getattr() function. 
# The getattr() function accepts an object and a variable name. 
# It returns the value of the class variable. For example:
extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')
print(extension, version)

# If the class variable doesn’t exist, you’ll also get an AttributeError exception. 
# To avoid the exception, you can specify a default value if the class variable doesn’t exist 
# like this:
media_type = getattr(HtmlDocument, 'media_type', 'text/html')
print(media_type)

""" Set values for class variables """

HtmlDocument.version = 10
print(HtmlDocument.version)

# You can use the setattr() built-in function:
setattr(HtmlDocument, 'version', 20)
print(HtmlDocument.version)

# Since Python is a dynamic language, you can add a class variable to a class at runtime 
# after you have created it. 
# For example, the following adds the media_type class variable to the HtmlDocument class:
class HtmlDocument:
    extension = 'html'
    version = 5

HtmlDocument.media_type = 'text/html'
print(HtmlDocument.media_type)

# Similarly, you can use the setattr() function:
setattr(HtmlDocument, media_type, 'text/html')
print(HtmlDocument.media_type)

""" Delete class variables """

# To delete a class variable at runtime, you use the delattr() function:
delattr(HtmlDocument, 'version')
# print(HtmlDocument.version)

# you can use the del keyword:
del HtmlDocument.media_type
# print(HtmlDocument.media_type)

""" Class variable storage """

# Python stores class variables in the __dict__ attribute. 
# The __dict__ is a mapping proxy, which is a dictionary. For example:

from pprint import pprint
class HtmlDocument:
    extension = 'html'
    version = '5'

HtmlDocument.media_type = 'text/html'
pprint(HtmlDocument.__dict__)

# Also, the key of the __dict__ are strings that will help Python speeds up the variable lookup.
# Although Python allows you to access class variables through the __dict__ dictionary, 
# it’s not a good practice. Also, it won’t work in some situations. For example:
print(HtmlDocument.__dict__['media_type']) # Bad Code

""" Callable class attributes """

# Class attributes can be any object such as a function.
# When you add a function to a class, the function becomes a class attribute. 
# Since a function is callable, the class attribute is called a callable class attribute. 
# For example:
from pprint import pprint
class HtmlDocument:
    extension = 'html'
    version = '5'

    def render():
        print('Rendering the Html doc...')

pprint(HtmlDocument.__dict__)

""" Summary """
# A class is an object which is an instance of the type class.
# Class variables are attributes of the class object.
# Use dot notation or getattr() function to get the value of a class attribute.
# Use dot notation or setattr() function to set the value of class attribute.
# Python is a dynamic language. Therefore, you can assign a class variable to a class at runtime.
# Python stores class variables in the __dict__ attribute. The __dict__ attribute is a dictionary.
