""" Python Data vs. Non-data Descriptors """
# Descriptors have two types:

# Data descriptors are objects of a class that implements __set__ method (and/or __delete__ method)
# Non-data descriptors are objects of a class that have the __get__ method only.

# Both descriptor types can optionally implement the __set_name__ method. The __set_name__ method doesn’t affect the classification of the descriptors.

# The descriptor types determine how Python resolves object’s attributes lookup.

""" Non-data descriptor"""
# If a class uses a non-data descriptor, Python will search the attribute in instance attributes 
# first (instance.__dict__). If Python doesn’t find the attribute in the instance attributes, 
# it’ll use the data descriptor.

import os
class FileCount:
    def __get__(self, instance, owner):
        print('The __get__ was called')
        return len(os.listdir(instance.path))

class Folder:
    count = FileCount()

    def __init__(self, path):
        self.path = path

folder = Folder('/')
print(folder.__dict__)
print('file count: ', folder.count)
print(folder.__dict__)

# After that, set the count attribute of the folder instance to 100 and access the count attribute:
folder.__dict__['count'] = 100
print(folder.__dict__)
print('file count: ', folder.count)
# In this example, Python can find the count attribute in the instance dictionary __dict__. 
# Therefore, it does not use data descriptors

""" Data descriptor """

# When a class has a data descriptor, Python will look for an instance’s attribute in the data 
# descriptor first. If Python doesn’t find the attribute, it’ll look for the attribute in the 
# instance dictionary (__dict__)

class Coordinate:
    def __get__(self, instance, owner):
        print('The __get__ was called')
    
    def __set__(self, instance, value):
        print('The __set__ was called')

class Point:
    x = Coordinate()
    y = Coordinate()

p = Point()
p.x = 10
print(p.x)

""" Summary """
# Data descriptors are objects of a class that implements __set__ method (and/or __delete__ method)
# Non-data descriptors are objects of a class that have the __get__ method only.
# When accessing object’s attributes, data descriptors override the instance’s attributes and 
# instance’s attributes override non-data descriptors.