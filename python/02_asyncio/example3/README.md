
### Parallelism: 
This involves executing multiple operations simultaneously. It refers to the ability to perform several tasks at the same time, improving efficiency and reducing the overall time taken to complete those tasks.

### Multiprocessing: This is a technique used to achieve parallelism by distributing tasks across a computer's central processing units (CPUs) or cores. Instead of relying on a single CPU to handle all operations, multiprocessing utilizes multiple CPUs or cores to work on different tasks simultaneously.

The paragraph emphasizes that multiprocessing is a method to achieve parallelism. It's particularly effective for tasks that heavily utilize the CPU, such as tasks involving intense calculations or tightly bound loops (loops that repeat a set of instructions for a specific number of iterations). These tasks can be split and distributed among multiple CPUs or cores, resulting in faster execution and better performance compared to executing them sequentially or on a single CPU/core.

### Concurrency 
Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

### Threading: 
Think of threading as a way for a computer to handle multiple tasks at the same time. Imagine multiple threads (like separate paths of execution) taking turns to do different jobs within a single process (which is like a container for these threads).

  - #### Python's GIL (Global Interpreter Lock): 
  Python has something called the Global Interpreter Lock, which affects how threads work in Python. It can sometimes limit the full potential of threading by allowing only one thread to execute Python bytecode at a time, especially in certain situations. However, we won't dive into the details here.
  
  - #### Threading and tasks: 
  Threading is particularly good for IO-bound tasks. Now, what does that mean?
    - **CPU-bound tasks**: 
    These are tasks that heavily use the computer's processing power. Imagine a task where the computer's cores are continuously busy, doing calculations or other intensive work from start to finish.
    - **IO-bound tasks**: These tasks spend a lot of time waiting for input/output operations to complete, like reading from or writing to a file, sending or receiving data over a network, or waiting for user input. Threading is useful for these tasks because while one thread waits for an input/output operation to finish, other threads can continue working on different tasks without being held up.

In simpler terms, threading is great for tasks that involve a lot of waiting, like reading files or communicating over the internet. While one part of the program is waiting for something to happen (like loading data from a file), other parts can keep doing their jobs, making the overall process more efficient.

### Python's Support: 
Python's standard library provides tools to handle both multiprocessing and threading. It offers modules like multiprocessing, threading, and concurrent.futures to facilitate these concurrent execution models. These packages enable developers to create programs that take advantage of multiprocessing or threading depending on the nature of the tasks they are dealing with.

### Introduction of Asynchronous IO (Async IO): 
Recently, Python, particularly CPython (the standard Python implementation), introduced a significant feature known as asynchronous IO. This functionality is facilitated through the asyncio package and the async and await keywords in the language.
  - #### Async IO and its Characteristics:
    - **Not Threading or Multiprocessing**: It's essential to clarify that async IO is distinct from both threading and multiprocessing. It doesn't rely on or build upon these concepts.
    - **Single-threaded, Single-process Design**: Async IO operates using a design that involves only one thread and one process. It utilizes a concept called "cooperative multitasking," which you'll explore further in the tutorial.
    - **Concurrent but not Parallel**: Async IO provides a sense of concurrency despite running on a single thread within a single process. It employs coroutines, a key aspect of async IO, that can be scheduled concurrently but aren't inherently concurrent by themselves.
  - #### Understanding Async IO as Concurrent Programming: 
  Async IO represents a style of concurrent programming, but it's important to note that it is not parallelism. While it shares some similarities with threading, it stands as a separate approach in the world of concurrency, distinct from both threading and multiprocessing.


### Core of Async IO: 
**Coroutines**: In the context of async IO in Python, coroutines are the central building blocks. A coroutine is a special kind of function, closely related to Python's generator functions.
  - #### Baseline Definition of Coroutines:
  Function with Suspension: A coroutine is a function that possesses the ability to pause its execution before it reaches the return statement.
  - #### Indirect Control Passing: 
  Additionally, a coroutine can indirectly transfer control to another coroutine for a certain period before resuming its execution.
  - #### Coroutines vs. Traditional Functions:
  Resumption of Execution: Unlike regular functions that execute and complete their tasks sequentially, coroutines have the ability to pause their execution, perform other tasks, and then resume from where they left off.
  - #### Facilitating Cooperation: 
  Coroutines can cooperate with each other by handing over control, enabling efficient multitasking and concurrency.
  - #### Understanding Coroutines through Generators:
    - **Repurposing Generators**: Coroutines are created using Python's generator functions, but they are enhanced to have additional capabilities beyond standard generators.

In summary, coroutines are special functions in Python used in async IO. They differ from regular functions by their ability to pause their execution, pass control to other coroutines, and resume from where they left off. Coroutines leverage the concepts of suspension and control passing to facilitate efficient cooperation among tasks, forming the foundation of async IO programming in Python.

### Introduction to async, await, and Coroutines:
- **async def Syntax**: The async def keyword combination is used to define functions that can act as coroutines in Python. These functions can contain await, return, or yield statements, but these are not mandatory.
- **async with and async for**: In addition to async def, Python supports async with and async for expressions, which will be explored later.
- **Role of await in Coroutines**: When encountered within a coroutine function (defined with async def), await is used to pause the execution of the surrounding coroutine. It passes control back to the event loop and indicates to the loop that it should suspend the current coroutine (g() in the example) until the awaited operation (f() in the example) is completed. During this suspension, other tasks can execute.
- **Calling Coroutines**: To execute a coroutine function, you need to use await to retrieve its results. You cannot directly call a coroutine function without using await.
- **yield and Async**: In async def blocks, using yield is less common and generally associated with creating asynchronous generators. It's advised to focus on understanding the syntax and usage of coroutine functions with await and/or return.

### Reference:
- https://realpython.com/async-io-python/