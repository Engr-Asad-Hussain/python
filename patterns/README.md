## Design Patterns
Design patterns are used to represent the pattern used by developers to create software or web application. These patterns are selected based on the requirement analysis. The patterns describe the solution to the problem, when and where to apply the solution and the consequences of the implementation.

## Model View Controller Pattern
- ```Model```: It consists of pure application logic, which interacts with the database. It includes all the information to represent data to the end user.
- ```View```: View represents the HTML files, which interact with the end user. It represents the model’s data to user.
- ```Controller```: It acts as an intermediary between view and model. It listens to the events triggered by view and queries model for the same.
- Reference(s):
  - https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_quick_guide.htm


## Singleton Pattern
- This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.
- It provides a global point of access to the instance created.
- The number of instances created are same and there is no difference in the objects listed in output.
- Reference(s):
  - https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_quick_guide.htm


## Factory Pattern
- The factory pattern comes under the creational patterns list category. It provides one of the best ways to create an object. In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface.
- Factory patterns are implemented in Python using factory method. When a user calls a method such that we pass in a string and the return value as a new object is implemented through factory method. The type of object used in factory method is determined by string which is passed through method.
- Reference(s):
  - https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_quick_guide.htm


## Builder
- Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach. This design pattern comes under the category of creational pattern. In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects.

## What's a design pattern?
Design patterns are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.

Reference(s):
  - https://refactoring.guru/design-patterns/what-is-pattern


## History of design pattern.
The concept of patterns was first described by ***Christopher Alexander*** in A Pattern Language: ```Towns```, ```Buildings```, ```Construction```. The book describes a “language” for designing the urban environment. The units of this language are patterns. They may describe how high windows should be, how many levels a building should have, how large green areas in a neighborhood are supposed to be, and so on.

The idea was picked up by four authors: *Erich Gamma*, *John Vlissides*, *Ralph Johnson*, and *Richard Helm*. In 1994, they published ***Design Patterns: Elements of Reusable Object-Oriented Software***, in which they applied the concept of design patterns to programming. The book featured 23 patterns solving various problems of object-oriented design and became a best-seller very quickly. Due to its lengthy name, people started to call it “***The Book by The Gang of Four***” which was soon shortened to simply “the GoF book”.

Since then, dozens of other object-oriented patterns have been discovered. The “pattern approach” became very popular in other programming fields, so lots of other patterns now exist outside of object-oriented design as well.

Reference(s):
  - https://refactoring.guru/design-patterns/history


## Classification of patterns
Design patterns differ by their complexity, level of detail and scale of applicability to the entire system being designed. I like the analogy to road construction: you can make an intersection safer by either installing some traffic lights or building an entire multi-level interchange with underground passages for pedestrians. This book covers three main groups of patterns:
  1. **Creational patterns** provide object creation mechanisms that increase flexibility and reuse of existing code.
  2. **Structural patterns** explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.
  3. **Behavioral patterns** take care of effective communication and the assignment of responsibilities between objects.

Reference(s):
  - https://refactoring.guru/design-patterns/classification


## The Catalog of Design Patterns
1. **Creational patterns**: These patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.
 - Factory Method
 - Abstract Factory
 - Builder
 - Prototype
 - Singleton

2. **Structural patterns**: These patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.
  - Adapter
  - Bridge
  - Composite
  - Decorator
  - Facade
  - Flyweight
  - Proxy

3. **Behavioral patterns**: These patterns are concerned with algorithms and the assignment of responsibilities between objects.
  - Chain of Responsibility
  - Command
  - Iterator
  - Mediator
  - Memento
  - Observer
  - State
  - Strategy
  - Template Method
  - Visitor

Reference(s):
  - https://refactoring.guru/design-patterns/catalog


### Factory Pattern
- Factory Method is a creational design pattern used to create concrete implementations of a common interface.
- It separates the process of creating an object from the code that depends on the interface of the object.
- For example, an application requires an object with a specific interface to perform its tasks. The concrete implementation of the interface is identified by some parameter.
- Instead of using a complex if/elif/else conditional structure to determine the concrete implementation, the application delegates that decision to a separate component that creates the concrete object. With this approach, the application code is simplified, making it more reusable and easier to maintain.
- Reference(s):
  - https://realpython.com/factory-method-python/