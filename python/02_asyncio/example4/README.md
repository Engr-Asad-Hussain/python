## Table of Content
- [Difference between CPU-Bound and I/O-Bound](#difference-between-cpu-bound-and-io-bound)
    - [CPU-Bound Task](#cpu-bound)
    - [I/O-Bound Task](#io-bound)
    - [Conclusion](#conclusion)


## Difference between CPU-Bound and I/O-Bound
### CPU-Bound
*When a program is CPU-bound*, it implies that the primary limiting factor affecting its performance is the processing power of the CPU (`Central Processing Unit`). In other words, the CPU is working at maximum capacity or close to it, and the program's speed and efficiency are constrained by the CPU's ability to execute instructions and process data. Tasks that are computationally intensive, such as complex mathematical calculations, heavy data manipulation, or extensive processing algorithms, can cause a program to become CPU-bound.

A program is *CPU bound* if it would go faster if the CPU is faster, i.e. it spends the majority of its time simply using the CPU (doing calculations). A program that computes new digits of ```π``` will typically be CPU-bound, it's just crunching numbers. A task that performs calculations on a small set of numbers, for example multiplying small matrices, is likely to be CPU bound.


### I/O-Bound
*When a program is I/O-bound*, it means that the program's performance is limited by the `input/output` operations it performs, rather than by the processing power of the CPU. These I/O operations typically involve reading from or writing to external resources like disk storage, network devices, databases, or other peripherals. Slow I/O operations, such as reading large files from disk, making network requests that take significant time, or waiting for user input, can lead to a program becoming I/O-bound. In such cases, the CPU might not be fully utilized because it spends a considerable amount of time waiting for I/O operations to complete.

A program is *I/O bound* if it would go faster if the I/O subsystem is faster. Which exact I/O system is meant can vary; I typically associate it with the disk, but of course, networking or communication, in general, is common too. A program that looks through a huge file for some data might become I/O bound since the bottleneck is that the reading of the data from disk. A task that processes data from disk, for example, counting the number of lines in a file is likely to be I/O bound.


### Conclusion
Understanding whether a program is CPU-bound or I/O-bound is crucial for optimizing its performance. For CPU-bound programs, optimizing algorithms or using parallel processing techniques might help improve performance. Meanwhile, for I/O-bound programs, strategies such as asynchronous I/O, caching, or optimizing data retrieval mechanisms can help enhance efficiency by reducing the time spent waiting for I/O operations to complete.


## Understanding Asynchronous Programming
A ***synchronous program*** is executed one step at a time. Even with conditional `branching`, `loops` and `function calls`, you can still think about the code in terms of taking one execution step at a time. When each step is complete, the program moves on to the next one.

Here are two examples of programs that work this way:
- **Batch processing programs** are often created as `synchronous programs`. You get some input, process it, and create some output. Steps follow one after the other until the program reaches the desired output. The program only needs to pay attention to the steps and their order.
- **Command-line programs** are small, quick processes that run in a terminal. These scripts are used to create something, transform one thing into something else, generate a report, or perhaps list out some data. This can be expressed as a series of program steps that are executed sequentially until the program is done.

In a *synchronous program*, if an execution step starts a database query, then the CPU is essentially idle until the database query is returned. For batch-oriented programs, this isn’t a priority most of the time. Processing the results of that IO operation is the goal. Often, this can take longer than the IO operation itself. Any optimization efforts would be focused on the processing work, not the IO.
Asynchronous programming techniques allow your programs to take advantage of relatively slow IO processes by freeing the CPU to do other work.

***An asynchronous program*** behaves differently. It still takes one execution step at a time. The difference is that the system may not wait for an execution step to be completed before moving on to the next one.

This means that the program will move on to future execution steps even though a previous step hasn’t yet finished and is still running elsewhere. This also means that the program knows what to do when a previous step does finish running.

Each section of code that runs independently is known as a thread, and all threads share the same memory space

## References:
- https://realpython.com/python-async-features/