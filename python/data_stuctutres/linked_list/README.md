## Linked List
> [!NOTE]
> Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

### Main Concepts
Before going more in depth on what linked lists are and how you can use them, you should first learn how they are structured. Each element of a linked list is called a ```node```, and every node has two different fields:
  1. ```Data``` contains the value to be stored in the node.
  2. ```Next``` contains a reference to the next node on the list.

> [!NOTE]
> A ```linked list``` is a collection of nodes. The first node is called the ```head```, and it’s used as the starting point for any iteration through the list. The last node must have its ```next``` reference pointing to ```None``` to determine the end of the list.
Here’s how it looks:

### Introducing collections.deque
In Python, there’s a specific object in the collections module that you can use for linked lists called deque (pronounced “deck”), which stands for double-ended queue.
```collections.deque``` uses an implementation of a linked list in which you can access, insert, or remove elements from the beginning or end of a list with constant ***O(1) performance***.
```py
from collections import deque

deque()
# deque([])

deque(['a','b','c'])
# deque(['a', 'b', 'c'])

deque('abc')
# deque(['a', 'b', 'c'])

empty = deque()
empty.append('a')
empty.append('b')
empty.append('c')
# deque(['a', 'b', 'c'])

empty.pop()
# deque(['a', 'b'])

empty.appendleft('1')
# deque(['1', 'a', 'b'])

empty.appendleft('2')
# deque(['2', '1', 'a', 'b'])

empty.popleft()
# deque(['1', 'a', 'b'])
```

### Practical Applications
Linked lists serve a variety of purposes in the real world. They can be used to implement (spoiler alert!) ```queues``` or ```stacks``` as well as ```graphs```. They’re also useful for much more complex tasks, such as lifecycle management for an operating system application.

### Queues
> [!NOTE]
> Queues and stacks differ only in the way elements are retrieved. For a ```queue```, you use a ```First-In/First-Out (FIFO)``` approach. 
That means that the first element inserted in the list is the first one to be retrieved. In the diagram above, you can see the ```front``` and ```rear``` elements of the queue. When you append new elements to the queue, they’ll go to the rear end. When you retrieve elements, they’ll be taken from the front of the queue.

For example, imagine a queue at a trendy and fully booked restaurant. If you were trying to implement a fair system for seating guests, then you’d start by creating a queue and adding people as they arrive:
```py
from collections import deque

queue = deque()
# deque([])

queue.append("Mary")
queue.append("John")
queue.append("Susan")
# deque(['Mary', 'John', 'Susan'])
```
Now you have Mary, John, and Susan in the queue. Remember that since queues are FIFO, the first person who got into the queue should be the first to get out.

Now imagine some time goes by and a few tables become available. At this stage, you want to remove people from the queue in the correct order. This is how you would do that:
```py
queue.popleft()
# 'Mary'

queue
# deque(['John', 'Susan'])

queue.popleft()
# 'John'

queue
# deque(['Susan'])
```
Every time you call ```popleft()```, you remove the head element from the linked list, mimicking a real-life queue.


### Stack
> [!NOTE]
> For a stack, you use a ```Last-In/Fist-Out (LIFO)``` approach, meaning that the last element inserted in the list is the first to be retrieved. 
In the above diagram you can see that the first element inserted on the stack (index 0) is at the bottom, and the last element inserted is at the top. Since stacks use the LIFO approach, the last element inserted (at the top) will be the first to be retrieved.

What if you wanted to create a stack instead? Well, the idea is more or less the same as with the queue. The only difference is that the stack uses the LIFO approach, meaning that the last element to be inserted in the stack should be the first to be removed.

Imagine you’re creating a web browser’s history functionality in which store every page a user visits so they can go back in time easily. Assume these are the actions a random user takes on their browser:
  - Visits Real Python’s website
  - Navigates to Pandas: How to Read and Write Files
  - Clicks on a link for Reading and Writing CSV Files in Python
If you’d like to map this behavior into a stack, then you could do something like this:
```py
>>> from collections import deque
>>> history = deque()

>>> history.appendleft("https://realpython.com/")
>>> history.appendleft("https://realpython.com/pandas-read-write-files/")
>>> history.appendleft("https://realpython.com/python-csv/")
>>> history
deque(['https://realpython.com/python-csv/',
       'https://realpython.com/pandas-read-write-files/',
       'https://realpython.com/'])
```

In this example, you created an empty history object, and every time the user visited a new site, you added it to your history variable using appendleft(). Doing so ensured that each new element was added to the head of the linked list.

Now suppose that after the user read both articles, they wanted to go back to the Real Python home page to pick a new article to read. Knowing that you have a stack and want to remove elements using LIFO, you could do the following:
```py
>>> history.popleft()
'https://realpython.com/python-csv/'

>>> history.popleft()
'https://realpython.com/pandas-read-write-files/'

>>> history
deque(['https://realpython.com/'])
```

### Implementing Your Own Linked List
(checkout the example data_stuctures/linked_list/own_linked_list.py)

- Reference(s):
  - https://realpython.com/linked-lists-python/
