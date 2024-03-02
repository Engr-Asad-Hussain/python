<!DOCTYPE html>
<html><head><style>
.red {
    color: red;
}
.blue {
    color: blue;
}
</style></head><body>

## Python Object-Oriented Programming
This Python OOP explains to you the Python object-oriented programming clearly so that you can apply it to develop software more effectively.

By the end of this Python OOP module, you’ll have good knowledge of object-oriented principles. And you’ll know how to use Python syntax to create reliable and robust software applications.

## Content
- Section 1. Classes and objects
  - [Introduction to Python Object-oriented programming]()


## Objects
- An object is a container that contains <span class="red">data</span> and <span class="red">functionality</span>.
- The <span class="red">data</span> represents the object at a particular moment in time. Therefore, the data of an object is called the <span class="red">state</span>. Python uses <span class="red">attributes<span> to model the state of an object.
- The <span class="red">functionality</span> represents the behaviors of an object. Python uses functions to model the behaviors. When a function is associated with an object, it becomes a <span class="red">method</span> of the object.
- In other words, an object is a container that contains the <span class="red">state</span> and <span class="red">methods</span>.
- Before creating objects, you define a class first. And from the class, you can create one or more objects. The objects of a class are also called <span class="red">instances</span> of a class.
- Everything in Python is an object, including classes.

## Class
- To define a <span class="red">class</span> in Python, you use the class keyword followed by the class name and a colon.
- By convention, you use capitalized names for classes in Python. If the class name contains multiple words, you use the <span class="red">CamelCase</span> format, for example <span class="red">SalesEmployee</span>.

When printing out the person object, you’ll see its name and memory address:
```py
<__main__.Person object at 0x000001C46D1C47F0>
```

## Class Variables
- Class variables are bound to the class. They’re shared by all instances of that class.

The following example adds the <span class="red">extension</span> and <span class="red">version</span> class variables to the <span class="red">HtmlDocument</span> class:
```py
class HtmlDocument:
    extension = 'html'
    version = 5
```
Both extension and version are the class variables of the HtmlDocument class. They’re bound to the HtmlDocument class.

### Get the values of class variables
To get the values of class variables, you use the dot notation <span class="red">(.)</span>. For example:
```py
HtmlDocument.extension # html
HtmlDocument.version # 5
```
If you access a class variable that doesn’t exist, you’ll get an <span class="red">AttributeError</span> exception. For example:
```py
HtmlDocument.media_type # AttributeError: type object 'HtmlDocument' has no attribute 'media_type'
```
Another way to get the value of a class variable is to use the <span class="red">getattr()</span> function. The getattr() function accepts an object and a variable name. It returns the value of the class variable. For example:
```py
extension = getattr(HtmlDocument, 'extension') # html
```
If the class variable doesn’t exist, you’ll also get an AttributeError exception. To avoid the exception, you can specify a <span class="red">default value</span> if the class variable doesn’t exist like this:
```py
media = getattr(HtmlDocument, 'media', 'text/html') # text/html
```

### Set values for class variables
To set a value for a class variable, you use the <span class="red">dot</span> notation:
```py
HtmlDocument.version = 10
```
or you can use the <span class="red">setattr()</span> built-in function:
```py
setattr(HtmlDocument, 'version', 10)
```
Since Python is a <span class="red">dynamic language</span>, you can add a class variable to a class at <span class="red">runtime</span> after you have created it. For example, the following adds the <span class="red">media_type</span> class variable to the <span class="red">HtmlDocument</span> class:
```py
HtmlDocument.media_type = 'text/html'
print(HtmlDocument.media_type)
```
Similarly, you can use the <span class="red">setattr()</span> function:
```py
setattr(HtmlDocument, media_type, 'text/html')
print(HtmlDocument.media_type)
```

### Delete class variables
To delete a class variable at runtime, you use the <span class="red">delattr()</span> function:
```py
delattr(HtmlDocument, 'version')
```
Or you can use the <span class="red">del</span> keyword:
```py
del HtmlDocument.version
```

## Class variable storage
Python stores class variables in the ```__dict__``` attribute. The __dict__ is a mapping proxy, which is a dictionary. For example:
```py
from pprint import pprint

class HtmlDocument:
    extension = 'html'
    version = '5'

HtmlDocument.media_type = 'text/html'
pprint(HtmlDocument.__dict__)

mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'media_type': 'text/html',
              'version': '5'})
```
As clearly shown in the output, the ```__dict__``` has three class variables: extension, media_type, and version besides other predefined class variables.

Python does not allow you to change the __dict__ directly. For example, the following will result in an error:
```py
HtmlDocument.__dict__['released'] = 2008
# TypeError: 'mappingproxy' object does not support item assignment
```
However, you can use the <span class="red">setattr()</span> function or dot notation to indirectly change the __dict__ attribute.

Also, the key of the __dict__ are strings that will help Python speeds up the variable lookup.

Although Python allows you to access class variables through the __dict__ dictionary, it’s not a good practice. Also, it won’t work in some situations. For example:
```py
print(HtmlDocument.__dict__['type']) # BAD CODE
```
When you add a function to a class, the function becomes a class attribute. Since a function is callable, the class attribute is called a callable class attribute.

## Instance Method
- By definition, a <span class="red">method</span> is a function that is bound to an <span class="red">instance</span> of a class.
- When you define a function inside a class, it’s purely a function. However, when you call the function via an instance of a class, the function becomes a method. Therefore, a method is a function that is bound to an instance of a class.
- A method has the first argument <span class="red">(self)</span> as the object to which it is bound.
- Python automatically passes the bound object to the method as the first argument. By convention, its name is self.

## Instance Variables
- In Python, <span class="red">class variables</span> are bound to a <span class="red">class</span> while <span class="red">instance variables</span> are bound to a <span class="red">specific instance of a class</span>. The instance variables are also called <span class="red">instance attributes.
- Python stores instance variables in the ```__dict__``` attribute of the instance. Each instance has its own ```__dict__``` attribute and the keys in this __dict__ may be different.
- When you access a variable via the instance, Python finds the variable in the __dict__ attribute of the instance. If it cannot find the variable, it goes up and look it up in the __dict__ attribute of the class.

The following defines a <span class="red">HtmlDocument</span> class with two class variables:

```py
from pprint import pprint

class HtmlDocument:
    version = 5
    extension = 'html'

pprint(HtmlDocument.__dict__)
print(HtmlDocument.extension) # html
print(HtmlDocument.version) # 5

mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'version': 5})
```
The HtmlDocument class has two class variables: <span class="red">extension</span> and <span class="red">version</span>. Python stores these two variables in the ```__dict__``` attribute.

When you access the class variables via the class, Python looks them up in the __dict__ of the class. The following creates a new instance of the <span class="red">HtmlDocument</span> class:
```py
home = HtmlDocument()
```
The <span class="red">home</span> is an <span class="red">instance</span> of the HtmlDocument class. It has its own ```__dict__``` attribute:

```py
pprint(home.__dict__) # {}
```
The ```home.__dict__``` is now empty. The home.__dict__ stores the instance variables of the home object like the ```HtmlDocument.__dict__``` stores the class variables of the HtmlDocument class.

Since a <span class="red">dictionary</span> is <span class="red">mutable</span>, you can mutate it e.g., adding a new element to the dictionary. Python allows you to access the class variables from an instance of a class. For example:
```py
print(home.extension)
print(home.version)
```
In this case, Python looks up the variables <span class="red">extension</span> and <span class="red">version</span> in ```home.__dict__``` first. If it doesn’t find them there, it’ll go up to the class and look up in the ```HtmlDocument.__dict__```

However, if Python can find the variables in the __dict__ of the instance, it won’t look further in the __dict__ of the class.

The following defines the <span class="red">version</span> variable in the home object:
```py
home.version = 6
print(home.__dict__)
```
Python adds the version variable to the ```__dict__``` attribute of the home object:
The __dict__ now contains one instance variable:

```py
{'version': 6}
```
If you access the version attribute of the home object, Python will return the value of the version in the ```home.__dict__``` dictionary:
```
print(home.version) # 6
```
If you change the class variables, these changes also reflect in the instances of the class:
```
HtmlDocument.media_type = 'text/html'
print(home.media_type) # text/html
```

## Class Methods
- <span class="red">Instance methods</span> are bound to a <span class="red">specific instance of a class</span>.
- Instance methods can access instance attributes within the same class. To invoke instance methods, you need to create the instance of a class first.
- To create the <span class="red">class method</span>, you place <span class="red">@classmethod</span> decorator above the method definition. Rename the <span class="red">self</span> parameter to <span class="red">cls</span> as a first parameter.
- Class methods can't access instance attributes. It can only access class attributes.
- To call the class methods you use classname followed by dot and then the method name ```ClassName.MethodName()```.
- When to use class methods?: You can use class methods for any methods that are not bound to a specific instance but the class. In practice, you often use class methods for methods that create an <span class="red">instance of the class</span>. When a method creates an instance of the class and returns it, the method is called a <span class="red">factory method</span>.
- Following is the difference between class methods and instance methods:
  S.No | Features | class methods | Instance methods
  -------- | -------- | -------- | --------
  1 | Binding |	Class	| An instance of the class 
  2 | Calling	| Class.method() | object.method()
  3 | Accessing	| Class attributes | Instance & class attributes
- Reference: https://www.pythontutorial.net/python-oop/python-class-methods/

## Encapsulation & Private Attributes
- <span class="red">Encapsulation</span> is one of the four fundamental concepts in object-oriented programming including <span class="red">abstraction</span>, <span class="red">encapsulation</span>, <span class="red">inheritance</span>, and <span class="red">polymorphism</span>.
- Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. This is known as <span class="red">information hiding</span>.
- Encapsulation is the packing of data and methods into a class so that you can hide the information and <span class="red">restrict access</span> from outside.
- The idea of information hiding is that if you have an attribute that isn’t visible to the outside, you can control the access to its value to make sure your object is always has a <span class="red">valid state</span>.
- <span class="red">Private attributes</span> can be only accessible from the methods of the class. In other words, they cannot be accessible from outside of the class. Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class. By convention, you can define a private attribute by prefixing a single underscore <span class="red">(_)</span> ```_attribute```.
- If you prefix an attribute name with double underscores <span class="red">(__)</span> like this: ```__attribute``` Python will automatically change the name of the __attribute to: ```_class__attribute```. This is called the <span class="red">name mangling</span> in Python. By doing this, you cannot access the ```__attribute``` directly from the outside of a class like: ```instance.__attribute```. However, you still can access it using the _class__attribute name: ```instance._class__attribute```
- Reference: https://www.pythontutorial.net/python-oop/python-private-attributes/


## Class Attributes
- A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the ```__init__()``` method.
- Use ```class_name.class_attribute``` or ```object_name.class_attribute``` to access the value of the class_attribute.
- When you access an attribute via an <span class="red">instance</span> of the class ```circle.pi``` Python searches for the attribute in the instance attribute list. If the instance attribute list doesn’t have that attribute, Python continues looking up the attribute in the <span class="red">class attribute</span> list. Python returns the value of the attribute as long as it finds the attribute in the instance attribute list or class attribute list. However, if you access an attribute directly ```Circle.pi```, Python directly searches for the attribute in the class attribute list.
- Use class attributes for <span class="red">storing class contants</span>, <span class="red">track data across all instances</span>, and <span class="red">setting default values for all instances of the class</span>.
  1. Since a constant doesn’t change from instance to instance of a class, it’s handy to store it as a class attribute.
  2. Tracking data across of all instances: When a new instance gets created, the constructor adds the instance to the list.
  3. Sometimes, you want to set a default value for all instances of a class. In this case, you can use a class attribute.
- Reference: https://www.pythontutorial.net/python-oop/python-class-attributes/


## Static Methods
- <span class="red">Static methods</span> aren’t bound to an <span class="red">object</span>. In other words, static methods cannot access and modify an object state.
- In addition, Python doesn’t implicitly pass the <span class="red">cls</span> parameter (or the <span class="red">self</span> parameter) to static methods. Therefore, static methods cannot access and modify the <span class="red">class’s state</span>.
- Use static methods to define <span class="red">utility</span> methods or group a logically related functions into a class.
- Use the <span class="red">@staticmethod</span> decorator to define a static method.
- Following is the difference between class methods and static methods:
  S.No | Class Methods	| Static Methods
  -------- | -------- | --------
  1 | Python implicitly pass the cls argument to class methods.	| Python doesn’t implicitly pass the cls argument to static methods
  2 | Class methods can access and modify the class state.	| Static methods cannot access or modify the class state.
  3 | Use @classmethod decorators to define class methods.	| Use @staticmethod decorators to define static methods.

## Property
- Use the Python <span class="red">property()</span> class to define a property for a class.
- Lets have a class with two attributes <span class="red">name</span> and <span class="red">age</span>. Since age is an instance of a class, you can assign it a new value using ```person.age = 12```. The following assignment is also technically valid ```person.age = -2``` but not logically. So, every time you need to check using <span class="red">if/else</span> condition ```person.age > 0```. To avoid the repetitive code you will use <span class="red">getter</span> and <span class="red">setter</span> methods in the ```Person``` class. But this strategy will not work with backward compatibility.
- By convention the getter and setter have the following name: ```get_<attribute>()``` and ```set_<attribute>()```.
- User property on the class variables for backward compatibility also. 
- ```property(fget=None, fset=None, fdel=None, doc=None)```
- Reference: 
  - https://www.pythontutorial.net/python-oop/python-properties/
  - https://realpython.com/python-property/


## Property Decorator
- You can user property on the class variables. To get the age of a Person object, you can use either the <span class="red">age</span> property or the <span class="red">get_age()</span> method. This creates an <span class="red">unnecessary redundancy</span>.
- To avoid redundancy you use <span class="red">@property</span> on getter (props) and <span class="red">@props.setter</span> on the setter.
- Use the <span class="red">@property</span> decorator to create a property for a class.
- You can create read-only property by creating only the getter property on the attribute.
- One of the most common <span class="red">use cases</span> of property() is building managed attributes that validate the input data before storing or even accepting it as a secure input.
- Using @props and @props.setter for multiple instance attributes, makes your code repetition and breaks the <span class="red">DRY (Don’t Repeat Yourself)</span> principle, so you would want to refactor this code to avoid it. To do so, you can abstract out the repetitive logic using a <span class="red">descriptor</span>. To avoid duplicating the logic, you may have a method that validates data and reuse this method in other properties. This approach will enable reusability. However, Python has a better way to solve this by using descriptors.
- Reference: 
  - https://www.pythontutorial.net/python-oop/python-property-decorator/
  - https://realpython.com/python-property/


## Raise Exceptions
- General syntax to raise an exception is ```raise [expression [from another_expression]]```
- Reference:
  - https://realpython.com/python-raise-exception/


## Inheritance
- <span class="red">Inheritance</span> allows a class to reuse existing attributes and methods of another class.
- The class that inherits from another class is called a <span class="red">child class</span>, a <span class="red">subclass</span>, or a <span class="red">derived class</span>.
- The class from which other classes inherit is call a <span class="red">parent class</span>, a <span class="red">super class</span>, or a <span class="red">base class</span>.
- Use ```isinstance()``` to check if an object is an instance of a class.
- Use ```issubclass()``` to check if a class is a subclass of another class.
- Use ```super()``` to call the methods of a parent class from a child class.
- Reference:
  - https://www.pythontutorial.net/python-oop/python-inheritance/
  - https://www.pythontutorial.net/python-oop/python-super/


## Overriding Methods & Attributes
- The <span class="red">overriding</span> method allows a child class to provide a specific implementation of a method that is already provided by one of its parent classes.
- Reference:
  - https://www.pythontutorial.net/python-oop/python-overriding-method/


## Slots
- Python uses dictionaries to store instance attributes of instances of a class. This allows you to dynamically add more attributes to instances at runtime but also create a memory overhead.
- Define ```__slots__``` in the class if a class only contains <span class="red">fixed (or predetermined) instance attributes</span>, you can use the slots to instruct Python to use a more compact data structure instead of dictionaries. The ```__slots__``` optimizes the memory if the class has many objects.
- Reference:
  - https://www.pythontutorial.net/python-oop/python-__slots__/


## Abstraction
- In object-oriented programming, an <span class="red">abstract class</span> is a class that cannot be <span class="red">instantiated</span>. However, you can create classes that <span class="red">inherit</span> from an abstract class.
- Abstract classes are classes that you cannot create <span class="red">instances from</span>.
- Typically, you use an abstract class to create a <span class="red">blueprint</span> for other classes.
- Similarly, an abstract method is an method without an implementation. An abstract class may or may not include abstract methods.
- Python doesn’t directly support abstract classes. But it does offer a module that allows you to define abstract classes. To define an abstract class, you use the <span class="red">abc (abstract base class)</span> module. The abc module provides you with the infrastructure for defining <span class="red">abstract base classes</span>.
- It is also very usefull in type checking.
- Reference:
  - https://www.pythontutorial.net/python-oop/python-abstract-class/
  - https://www.youtube.com/watch?v=xvb5hGLoK0A


## Protocols
- Use Python ```Protocol``` to define implicit interfaces.
- In ```duck typing```, the behaviors and properties of an object determine the object type, not the explicit type of the object.
- The duck typing is inspired by the duck test: ```If it walks like a duck and its quacks like a duck, then it must be a duck```.
- When we use Protocols then there is no more import dependencies.
- Protocols were introduced in Python 3.8 as an alternative to Python ABC and they are differently in typing point of view. ABC classes relay on the nominal typing that means if you want typing relationship be there ```A is type(B)``` then you need to explicitly write down in your code for example using inheritance. So, you have abstract base class, you create subclasses from that abstract base class, you inherit from it and establish a relationship. Python interpreter uses that relationship to determine whether or not the types matched. Protocols are different, they relay on the structure typing and that means instead of having explicitly defining typing (A is of Protocol), Python looks at how the structure is of these objects. Do they have the same method? Do they have the same properties? If so, it will assume that the types matched. So that means that the usage of Protocols is actually also quite different. You don't establish generally inheritance relationships with them you don't inherit from a protocol class but the  protocol defines the interface that is expected in the part of program that refers to it. So, if you have a function or method in a class that gets an argument of a particular protocol type then anything that implements those methods that hase those properties can be passed as an argument to that function or method and structure typing that will actually do the comparsion of the structure of the objects is going to make sure that program works as expected to. This fits very will with the Python runtime type checking system that treats two objects the same if they have the same methods and properties that also called duct typing. 
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-protocol/
  - https://www.youtube.com/watch?v=xvb5hGLoK0A&t=452s
  - https://www.arjancodes.com/mindset/type-hints


## Enums (Enumerations)
- An <span class="red">enumeration</span> is a set of members that have associated unique constant values.
- Create a new enumeration by defining a class that inherits from the Enum type of the ```enum``` module.
- The members have the same types as the enumeration to which they belong.
- Use the ```enumeration[member_name]``` to access a member by its name and ```enumeration(member_value)``` to access a member by its value.
- Enumerations are <span class="red">iterable</span>.
- Enumeration members are <span class="red">hashable</span>.
- Enumerable are <span class="red">immuable</span>.
- Cannot inherits from an enumeration unless it has <span class="red">no</span> members.
- When an enumeration has different members with the same values, the first member is the main member while others are aliases of the main member.
- Use the ```@enum.unique``` decorator from the enum module to enforce the uniqueness of the values of the members.
- Use enum ```auto()``` class to generate unique values for enumeration members.
- Python enumerations are classes. It means that you can add methods to them, or implement the dunder methods to customize their behaviors. ```__str__```, ```__eq__```, ```__lt__```, ```__bool__```. Define an emum class with no members and methods and extends this base class.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-enumeration/
  - https://www.pythontutorial.net/python-oop/python-enum-unique/
  - https://www.pythontutorial.net/python-oop/python-enum-class/


## Multiple Inheritance
- When a class inherits from a single class, you have single inheritance. Python allows a class to inherit from <span class="red">multiple classes</span>. If a class inherits from two or more classes, you’ll have multiple inheritance. ```class ChildClass(ParentClass1, ParentClass2, ParentClass3):```
- Python multiple inheritance allows one class to inherit from multiple classes.
- The <span class="red">Method Order Resolution(MRO)</span> defines the class search path to find the method to call. To get the MRO of the inherited class you can use ```class_name.__mro__```. When the parent classes have methods with the same name and the child class calls the method, Python uses the method resolution order (MRO) to search for the right method to call.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-multiple-inheritance/

## Mixin
- A <span class="red">mixin</sapn> class provides method implementions for <span class="red">resuse</span> by multiple related subclasses.
- A mixin is a class that provides method implementations for reuse by multiple related child classes. However, the inheritance is not implying an <span class="red">is-a relationship</span>.
- A mixin doesn’t define a <span class="red">new type</span>. Therefore, it is not intended for direction <span class="red">instantiation</span>(```mx_instance = MixinClass()```)
- A mixin bundles a set of methods for reuse. Each mixin should have a single specific behavior, implementing closely related methods.
- Typically, a child class uses multiple inheritance to combine the mixin classes with a parent class.
- Since Python doesn’t define a formal way to define mixin classes, it’s a good practice to name mixin classes with the <span class="red">suffix Mixin</span>.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-mixin/


## Descriptors
- Suppose you have a ```class Person``` with two instance attributes ```first_name``` and ```last_name``` And you want the first_name and last_name attributes to be non-empty strings. These plain attributes cannot guarantee this. To enforce the ```data validity``` you can use ```@property``` with a getter and setter methods. This code works perfectly fine. However, it is ```redundant``` because the validation logic validates the ```first``` and ```last``` names is the same. Also, if the class has more attributes that require a non-empty string, you need to duplicate this logic in other properties. In other words, this validation logic is not reusable. To avoid duplicating the logic, you may have a method that validates data and reuse this method in other properties. This approach will enable reusability. However, Python has a better way to solve this by using ```descriptors```.
- In Python, the descriptor protocol consists of three methods: 
  - ```__get__``` gets an attribute value.
  - ```__set__``` sets an attribute value.
  - ```__delete__``` deletes an attribute. 
  - Optionally, a descriptor can have the ```__set_name__``` method that sets an attribute on an instance of a class to a new value.
- A descriptor is an object of a class that implements one of the methods specified in the descriptor protocol.
- Descriptors have two types: ```data descriptor``` and ```non-data descriptor```.
  - A ```data descriptor``` is an object of a class that implements the ```__set__``` and/or ```__delete__``` method.
  - A ```non-data descriptor``` is an object that implements the ```__get__``` method only.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-descriptors/


## Dataclasses
- Let say you have ```class Person``` has the ```__init__``` method that initializes the ```name``` and ```age``` attributes. If you want to have a string representation of the Person object, you need to implement the ```__str__``` or ```__repr__``` method. Also, if you want to compare two instances of the Person class by an attribute, you need to implement the ```__eq__``` method. However, if you use the ```dataclass```, you’ll have all of these features (and even more) without implementing these dunder methods.
- The dataclasses module has the ```astuple()``` and ```asdict()``` functions that convert an instance of the dataclass to a tuple and a dictionary.
- To create readonly objects from a dataclass, you can set the frozen argument of the dataclass decorator to True i.e., ```@dataclass(frozen=True)```.
- If don’t want to initialize an attribute in the __init__ method, you can use the field() function from the dataclasses module. Use __post_init__ method to initalize attributes that depends on other attributes.
- By default, a dataclass implements the __eq__ method. To allow different types of comparisons like __lt__, __lte__, __gt__, __gte__, you can set the order argument of the @dataclass decorator to True i.e., ```@dataclass(order=True)```.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-dataclass/
  - https://www.youtube.com/watch?v=CvQ7e6yUtnw

