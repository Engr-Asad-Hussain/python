### Threads processes Vs Asynchronous:
The traditional way of dealing with asynchronous and parallel code is by using threads. Whenever you start an application, this actually lauches a process. That's the operating system does that for you. 

### What is a process?
A process is basically a peice of CPU and memory that you get allocated. Within a process, you can have one or more threads, the operating system schedules, how much CPU time each process gets, and for how long. 

### What's the difference between threads and process?
Well processes get a separate piece of memory assigned to them. Whereas threads can acutally share memory. Threads are acutally quite useful because often you have to wait for things. For example, when you open a file, you have to wait untill the data becomes available, or you have to wait for the response of a network. And with threads this means you can do other things while you wait. 

### Problems with the threads?
Even though threads are quite powerful, there are couple of problems with them. 
- One problem is that because they share memory, you easily get race condition blocks where threads try to read/write data at the same time, leading to all kinds of unpredictable behaviour crashes.
- Another problem is that, programs in general becomes harder to understand if you have multiple threads, because as a developer, you have to think about what it means when the different threads interact with each other. So that means that even though you can create a program that is multi-threaded, it doesn't have to mean that in every program you just have to use the threads just because you know it, beacause they complicate things. 
- And a third issue is, it introduces some overhead beacause there is a part of the system that has to manage the threads lifecycle, stop them, restart them etc. And that also takes CPU time. 

### Asynchronous programming:
There is an alternative to threads and that's called asynchronous programming. This relies on something we call future or a promise or a delay or a deffered and these things describe a sort of proxy for an object that is at the moment yet unknown, and its going to be resolve later in the future. Normally, because the computation of that object has not yet been completed. In JavaScript these things are called as promises, in Python they called futures. They are not exactly the same, there is slightly difference between them, but are more or less the same way. But generally when you write asynchronous program, whether its a JavaScript or Python, you won't very often encounter these objects directly. Because there are syntax extensions that helps you write code that uses them, but you don't have to create these objects yourself. 

### Futures and promises:
Futures and promises comes from functional programming. These terms are already appeared in computer science academic papers in the 70s. Actually Barbara Liskov, whom you might known the Liskov Substition Priciple of SOLID Principles, has play a key role in defining futures and promises and how they should be used. 

Especially in Python 3.10, asynchronous operations have become a lot easier to deal with in your code. When you want to run on asynchronous program you can use asyncio to achieve that very easily.

### Reference(s)
https://www.youtube.com/watch?v=2IW-ZEui4h4&t=735s&ab_channel=ArjanCodes
