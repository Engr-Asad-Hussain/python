## Multiprocessing
Multiprocessing allows a program to run multiple processes in parallel, each with its own memory space. Unlike threads, which share the same memory space within a single process, processes are completely separate. This means multiprocessing is better suited for CPU-bound tasks where you want to take advantage of multiple CPU cores.

#### What is Multiprocessing?
Multiprocessing uses multiple processes to perform tasks in parallel, allowing true parallelism and better utilization of multi-core CPUs.

#### When to Use Multiprocessing?
Use multiprocessing when you have CPU-bound tasks that require heavy computation and can benefit from parallel execution. Examples include data processing, image processing, or any task that can be divided into independent subtasks.

#### Impact of Multiprocessing:
Multiprocessing can significantly speed up CPU-bound tasks by leveraging multiple CPU cores. However, it can also increase memory usage and overhead due to process creation and inter-process communication.

#### When Not to Use Multiprocessing:
Avoid multiprocessing for I/O-bound tasks or when the overhead of process creation outweighs the benefits. For I/O-bound tasks, asynchronous programming or threading is often more suitable.

> [!NOTE] Navigate to asyncio module to understand more about concurrency, parallelism, threading and multiprocessing.