""" Introduction to the Python Multiple inheritance """
# When a class inherits from a single class, you have single inheritance. 
# Python allows a class to inherit from multiple classes. 
# If a class inherits from two or more classes, you’ll have multiple inheritance.

class Car:
    def go(self):
        print('Going ...')

class Flyable:
    def fly(self):
        print('Flying ...')

class FlyingCar(Car, Flyable):
    # Since the FlyingCar inherits from Car and Flyable classes, it reuses the methods from those classes. 
    # It means you can call the go() and fly() methods on an instance of the FlyingCar class like this
    pass

fc = FlyingCar()
fc.go()
fc.fly()

""" Method resolution order (MRO) """
# When the parent classes have methods with the same name and the child class calls the method, 
# Python uses the method resolution order (MRO) to search for the right method to call. 
# Consider the following example

class Car:
    def start(self):
        print('start car object')
    
    def go(self):
        print('Going ...')

class Flyable:
    def start(self):
        print('start flyable object')
    
    def fly(self):
        print('Flying ...')

class FlyingCar(Flyable, Car):
    def start(self):
        super().start()

car = FlyingCar()
car.start()
print(FlyingCar.__mro__)

# If you flip the order of Flyable and Car classes in the list, the __mro__ will change accordingly.

""" Multiple inheritance & super """

class Car:
    def __init__(self, door, wheel):
        self.door = door
        self.wheel = wheel
    
    def start(self):
        print('start the car')
    
    def go(self):
        print('Going ...')

class Flyable:
    def __init__(self, wing):
        self.wing = wing

    def start(self):
        print('start the flyable')
    
    def fly(self):
        print('Flying ...')

class FlyingCar(Flyable, Car):
    def __init__(self, door, wheel, wing):
        super().__init__(wing=wing)
        self.door = door
        self.wheel = wheel
    
    def start(self):
        super().start()

print(FlyingCar.__mro__)

# the super().__init__() calls the __init__ of the FlyingCar class. 
# Therefore, you need to pass the wing argument to the __init__ method.

# Because the FlyingCar class cannot access the __init__ method of the Car class, you need to initialize 
# the door and wheel attributes individually.

""" Summary """
# Python multiple inheritance allows one class to inherit from multiple classes.
# The method order resolution defines the class search path to find the method to call.