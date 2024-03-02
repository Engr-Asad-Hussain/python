## SOLID Principles
- SOLID is an abbreviation that stands for five software design principles compiled by Uncle Bob:
  - ```S``` – Single responsibility Principle
  - ```O``` – Open-closed Principle
  - ```L``` – Liskov Substitution Principle
  - ```I``` – Interface Segregation Principle
  - ```D``` – Dependency Inversion Principle
- The single responsibility is the first principle in the SOLID principles.
- When you build a Python project using object-oriented programming (OOP), planning how the different classes and objects will interact to solve your specific problems is an important part of the job. This planning is known as ```object-oriented design (OOD)```, and getting it right can be a challenge. If you’re stuck while designing your Python classes, then the SOLID principles can help you out.
- SOLID is a set of five object-oriented design principles that can help you write more maintainable, flexible, and scalable code based on well-designed, cleanly structured classes. These principles are a fundamental part of object-oriented design best practices.
- A complete example that follows all the 5 fundamental principles of SOILD ```./solid_principles.py```.
- Reference(s):
  - https://realpython.com/solid-principles-python/
  - https://www.pythontutorial.net/python-oop/python-single-responsibility-principle/
  - https://www.youtube.com/watch?v=pTB30aXS77U&t=70s

## Single Responsibility Principle
- The single responsibility principle (SRP) states that every class, method, and function should have only one job or one reason to change.
- To make it more convenient, you can use the facade pattern so that the ```Person``` class will be the facade for the ```PersonDB``` class.
- The single-responsibility principle (SRP) comes from ```Robert C. Martin```, more commonly known by his nickname ```Uncle Bob```, who’s a well-respected figure in the software engineering world and one of the original signatories of the Agile Manifesto. In fact, he coined the term ```SOLID```. The single-responsibility principle states that: ```A class should have only one reason to change```. This means that a class should have only one ```responsibility```, as expressed through its ```methods```. If a class takes care of more than one task, then you should separate those tasks into separate classes. This principle is closely related to the concept of ```separation of concerns```, which suggests that you should split your programs into different sections. Each section must address a separate concern.
- The concept of responsibility in this context may be pretty subjective. Having a single responsibility doesn’t necessarily mean having a single method. Responsibility isn’t directly tied to the number of methods but to the core task that your class is responsible for, depending on your idea of what the class represents in your code. However, that subjectivity shouldn’t stop you from striving to use the SRP.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-single-responsibility-principle/
  - https://realpython.com/solid-principles-python/#single-responsibility-principle-srp
  - https://www.youtube.com/watch?v=pTB30aXS77U&t=70s


## Open-close Principle
- The open-closed principle allows you to design the system so that it is open for extension but closed for modification. The purpose of the open-closed principle is to make it easy to add new features (or use cases) to the system without directly modifying the existing code.
- The open-closed principle (OCP) for object-oriented design was originally introduced by ```Bertrand Meyer``` in 1988 and means that: ```Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification```.
- We usually use abstraction to achieve the open-close principle.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-open-closed-principle/
  - https://realpython.com/solid-principles-python/#open-closed-principle-ocp
  - https://www.youtube.com/watch?v=pTB30aXS77U&t=70s


## Liskov Substitution Principle
- The Liskov substitution principle states that a child class must be substitutable for its parent class. Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.
- The ```Liskov substitution principle (LSP)``` was introduced by ```Barbara Liskov``` at an OOPSLA conference in 1987. Since then, this principle has been a fundamental part of object-oriented programming. The principle states that: ```Subtypes must be substitutable for their base types```. For example, if you have a piece of code that works with a Shape class, then you should be able to substitute that class with any of its subclasses, such as Circle or Rectangle, without breaking the code.
- In practice, this principle is about making your subclasses behave like their base classes without breaking anyone’s expectations when they call the same methods. 
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-liskov-substitution-principle/
  - https://realpython.com/solid-principles-python/#liskov-substitution-principle-lsp
  - https://www.youtube.com/watch?v=pTB30aXS77U&t=70s


## Interface Segregation Principle
- The ```interface segregation principle``` advises that the interfaces should be small in terms of cohesions. Make fine grained interfaces that are client-specific. Clients should not be forced to implement interfaces they ```do not use```.
- An ```interface``` is a description of behaviors that an object can do. For example, when you press the power button on the TV remote control, it turns the TV on, and you don’t need to care how. In object-oriented programming, an interface is a set of ```methods``` an object must-have. The purpose of interfaces is to allow clients to request the correct methods of an object via its interface.
- Python uses ```abstract classes``` as interfaces because it follows the so-called duck typing principle. The duck typing principle states that “if it walks like a duck and quacks like a duck, it must be a duck.” In other words, the methods of a class determine what its objects will be, not the type of the class.
- The interface segregation principle (ISP) comes from the same mind as the single-responsibility principle. Yes, it’s another feather in ```Uncle Bob’s cap```. The principle’s main idea is that: ```Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies```. In this case, ```clients are classes and subclasses```, and ```interfaces consist of methods and attributes```. In other words, if a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into more specific classes.
- Reference(s)
  - https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/
  - https://realpython.com/solid-principles-python/#interface-segregation-principle-isp
  - https://www.youtube.com/watch?v=pTB30aXS77U&t=70s


## Dependency Inversion Principle
- The dependency inversion principle states that: 
  - High-level modules should not depend on low-level modules. Both should depend on abstractions
  - Abstractions should not depend on details. Details should depend on abstractions.
- The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them.
- It states that: ```Abstractions should not depend upon details. Details should depend upon abstractions```.
- Reference(s):
  - https://www.pythontutorial.net/python-oop/python-dependency-inversion-principle/
  - https://realpython.com/solid-principles-python/#dependency-inversion-principle-dip
  - https://www.youtube.com/watch?v=pTB30aXS77U&t=70s