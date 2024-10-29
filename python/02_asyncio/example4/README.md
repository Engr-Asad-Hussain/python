## Table of Content
- [Difference between CPU-Bound and I/O-Bound](#difference-between-cpu-bound-and-io-bound)
    - [CPU-Bound Task](#cpu-bound)
    - [I/O-Bound Task](#io-bound)
    - [Conclusion](#conclusion)


## Difference between CPU-Bound and I/O-Bound
### CPU-Bound
> *When a program is CPU-bound*, it implies that the primary limiting factor affecting its performance is the processing power of the CPU (`Central Processing Unit`). In other words, the CPU is working at maximum capacity or close to it, and the program's speed and efficiency are constrained by the CPU's ability to execute instructions and process data. Tasks that are computationally intensive, such as complex mathematical calculations, heavy data manipulation, or extensive processing algorithms, can cause a program to become CPU-bound.

#### Characteristics of CPU-Bound Tasks
- High CPU utilization.
- Limited by the speed of the processor, not by waiting for external resources.
- Longer execution time if the task involves extensive calculations.

#### Examples of CPU-Bound Tasks
1. ***Complex Calculations***: Calculating the Fibonacci sequence or performing recursive calculations.
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
This recursive function requires significant CPU time as n grows, making it CPU-bound.

2. ***Data Processing***: Processing large datasets, such as image or video processing.
```python
from PIL import Image

def resize_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size)
    img.save('resized_image.jpg')
```
Here, resizing an image requires CPU power, especially for large images or complex transformations.

3. ***Encryption and Compression***: Encrypting data or compressing files.
```python
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```
This function requires CPU to compute the hash, especially when processing many passwords.

#### Optimizing CPU-Bound Tasks
- **Parallel Processing**: Use multiple CPU cores with `multiprocessing` (like Python’s multiprocessing library) to distribute tasks across cores.
- **Compiled Languages**: Offload computationally heavy parts of the program to languages like C or C++ or use libraries that leverage optimized C extensions (like numpy).
- **Batch Processing**: Process large datasets in batches to avoid overwhelming the CPU with a single large task.


### I/O-Bound
> *When a program is I/O-bound*, it means that the program's performance is limited by the `input/output` operations it performs, rather than by the processing power of the CPU. These I/O operations typically involve reading from or writing to external resources like disk storage, network devices, databases, or other peripherals. Slow I/O operations, such as reading large files from disk, making network requests that take significant time, or waiting for user input, can lead to a program becoming I/O-bound. In such cases, the CPU might not be fully utilized because it spends a considerable amount of time waiting for I/O operations to complete.

#### Characteristics of I/O-Bound Tasks**
- High latency due to waiting for external resources.
- Limited by I/O speeds, such as disk read/write speeds or network latency.
- Low CPU usage because most of the time is spent in waiting, not processing.

#### Examples of I/O-Bound Tasks**
1. ***Database Queries***: Fetching data from a database and processing the results.
```python
import psycopg2

def get_user_data(user_id):
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    data = cur.fetchone()
    conn.close()
    return data
```
Here, the function is limited by the time it takes to connect to the database, query, and fetch results, not by processing power.

2. ***File I/O***: Reading and writing large files.
```python
def process_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data
```
The function spends most of its time waiting for the file data to be read from disk.

3. ***Network Requests***: Making API calls or requests to external servers.
```python
import requests

def fetch_api_data(url):
    response = requests.get(url)
    return response.json()
```
This function waits for data from a network, making it I/O-bound.

#### Optimizing I/O-Bound Tasks
- **Concurrency**: Use `threading` or `asynchronous` programming (like asyncio in Python) to handle multiple I/O-bound tasks concurrently.
- **Asynchronous** Libraries: For example, using aiohttp for network requests or asyncpg for async database queries in Python.


### Choosing Concurrency Models Based on Task Type
- **I/O-Bound**: For I/O-bound tasks, concurrency (like asynchronous programming or multithreading) is often more effective because you can execute other tasks while waiting for I/O operations. `Example`: Using asyncio in Python to handle network requests concurrently:
```python
import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = ['http://example.com/api1', 'http://example.com/api2']
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

- **CPU-Bound**: For CPU-bound tasks, multiprocessing is more effective because it allows you to take advantage of multiple CPU cores by running separate processes. `Example`: Using Python’s multiprocessing to parallelize a CPU-intensive task:
```python
from multiprocessing import Pool

def compute_square(n):
    return n * n

if __name__ == '__main__':
    with Pool(4) as pool:  # Create a pool with 4 processes
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(compute_square, numbers)
    print(results)
```
Understanding these distinctions lets you optimize your application by choosing the right concurrency model for each task type, improving both performance and resource utilization.


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