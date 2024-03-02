""" Introduction to the Python methods """

# By definition, a method is a function that is bound to an instance of a class. 
# This tutorial helps you understand how it works under the hood.

class Request:
    def send():
        print('sending ...')

# And you can call the send() function via the Request class like this:
Request.send()
print(Request.send) # function: not bounded with the instance of a class
print(type(Request.send))

# The following creates a new instance of the Request class:
http_request = Request()
print(http_request.send) # method: bound to the instance of a class

# So the http_request.send is not a function like Request.send. 
# The following checks if the Request.send is the same object as http_request.send. 
# It’ll returns False as expected:
print(type(http_request.send) is (Request.send))

# The following redefines the Request class where the send function accepts a list of arguments:
class Request:
    def send(*args):
        print(args)

http_request = Request()
print(http_request.send())

# For this reason, a method of an object always has the object as the first argument. By convention, it is called self:
class Request:
    def send(self):
        print('sending ...')

http_request = Request()
http_request.send()

""" Summary """
# When you define a function inside a class, it’s purely a function. However, when you call the function via an instance of a class, the function becomes a method. Therefore, a method is a function that is bound to an instance of a class.
# A method is an instance of the method class.
# A method has the first argument (self) as the object to which it is bound.
# Python automatically passes the bound object to the method as the first argument. By convention, its name is self.