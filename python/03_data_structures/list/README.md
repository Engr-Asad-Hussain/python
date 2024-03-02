## List
> [!NOTE]
> Python’s list is a flexible, versatile, powerful, and popular built-in data type. It allows you to create variable-length and mutable sequences of objects. In a list, you can store objects of any type. You can also mix objects of different types within the same list, although list elements often share the same type.

Some of the more relevant characteristics of list objects include being:

- **Ordered**: They contain elements or items that are sequentially arranged according to their specific insertion order.
- **Zero-based**: They allow you to access their elements by indices that start from zero.
- **Mutable**: They support in-place mutations or changes to their contained elements.
- **Heterogeneous**: They can store objects of different types.
- **Growable and dynamic**: They can grow or shrink dynamically, which means that they support the addition, insertion, and removal of elements.
- **Nestable**: They can contain other lists, so you can have lists of lists.
- **Iterable**: They support iteration, so you can traverse them using a loop or comprehension while you perform operations on each of their elements.
- **Sliceable**: They support slicing operations, meaning that you can extract a series of elements from them.
- **Combinable**: They support concatenation operations, so you can combine two or more lists using the concatenation operators.
- **Copyable**: They allow you to make copies of their content using various techniques.

In Python, lists are ordered, which means that they keep their elements in the order of insertion:
```py
>>> colors = [
...     "red",
...     "orange",
...     "yellow",
...     "green",
...     "blue",
...     "indigo",
...     "violet"
... ]

>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
```
The items in this list are strings representing colors. If you access the list object, then you’ll see that the colors keep the same order in which you inserted them into the list. This order remains unchanged during the list’s lifetime unless you perform some mutations on it.

## Heterogeneous 
Lists can contain objects of different types. That’s why lists are heterogeneous collections:
```py
[42, "apple", True, {"name": "John Doe"}, (1, 2, 3), [3.14, 2.78]]
```

## Naming Convention
Note that naming lists as plural nouns is a common practice that improves readability. However, there are situations where you can use collective nouns as well.

For example, you can have a list called ```people```. In this case, every item will be a person. Another example would be a list that represents a ```table``` in a database. You can call the list table, and each item will be a row.


## Considering Performance While Growing Lists
When you create a list, Python allocates enough space to store the provided items. It also allocates extra space to host future items. When you use the extra space by adding new items to that list with ```.append()```, ```.extend()```, or ```.insert()```, Python automatically creates room for additional new items.

This process is known as **resizing**, and while it ensures that the list can accept new items, it requires **extra CPU time** and **additional memory**. Why? Well, ```to grow an existing list, Python creates a new one with room for your current data and the extra items. Then it moves the current items to the new list and adds the new item or items.```

Consider the following code to explore how Python grows a list dynamically:
```py
>>> from sys import getsizeof


>>> numbers = []
>>> for value in range(100):
...     print(f"{numbers=} | {getsizeof(numbers)=} bytes")
...     numbers.append(value)
...
numbers=[] | getsizeof(numbers)=56 bytes
numbers=[0] | getsizeof(numbers)=88 bytes
numbers=[0, 1] | getsizeof(numbers)=88 bytes
numbers=[0, 1, 2] | getsizeof(numbers)=88 bytes
numbers=[0, 1, 2, 3] | getsizeof(numbers)=88 bytes
numbers=[0, 1, 2, 3, 4] | getsizeof(numbers)=120 bytes
numbers=[0, 1, 2, 3, 4, 5] | getsizeof(numbers)=120 bytes
numbers=[0, 1, 2, 3, 4, 5, 6] | getsizeof(numbers)=120 bytes
numbers=[0, 1, 2, 3, 4, 5, 6, 7] | getsizeof(numbers)=120 bytes
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8] | getsizeof(numbers)=184 bytes
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] | getsizeof(numbers)=184 bytes
...
```
In this code snippet, you first import ```getsizeof()``` from the ```sys``` module. This function allows you to get the size of an object in bytes. Then you define numbers as an empty list.

> [!IMPORTANT]
> Inside the for loop, you get and print your list object’s size in bytes. The first iteration shows that the size of your empty list is ```56 bytes```, which is the baseline size of every list in Python.

> [!IMPORTANT]
> Next, the ```.append()``` method adds a new value to your list. Note how the size of numbers grows to ```88 bytes```. That’s the baseline size plus 32 additional bytes (56 + 4 × 8 = 88), which represent ```four 8-byte pointers or slots for future items```. It means that Python went ahead and allocated space for four items when you added the first element.

> [!NOTE]
> As the loop goes, the size of numbers grows to ```120 bytes```, which is 88 + 4 × 8 = 120. This step allocates space for four more items. That’s why you get 120 four times on your screen.

> [!WARNING]
> If you follow the loop’s output, then you’ll notice that the next steps add room for ```eight extra items```, then for ```twelve```, then for ```sixteen```, and so on. ***Every time Python resizes the list, it has to move all the items to the new space, which takes considerable time***.

In practice, if you’re working with small lists, then the overall impact of this internal behavior is negligible. However, in performance-critical situations or when your lists are large, you may want to use more efficient data types, such as ```collections.deque```, for example.


## Deciding Whether to Use Lists
As you’ve learned throughout this tutorial, lists are powerful, flexible, versatile, and full-featured data structures. Because of their characteristics, people tend to use and abuse them. Yes, they’re suitable for many use cases, but sometimes they aren’t the best available option.

In general, you should use lists when you need to:
- **Keep your data ordered**: Lists maintain the order of insertion of their items.
- **Store a sequence of values**: Lists are a great choice when you need to store a sequence of related values.
- **Mutate your data**: Lists are mutable data types that support multiple mutations.
- **Access random values by index**: Lists allow quick and easy access to elements based on their index.

In contrast, avoid using lists when you need to:
- **Store immutable data**: In this case, you should use a ```tuple```. They’re immutable and more memory efficient.
- **Represent database records**: In this case, consider using a ```tuple``` or a ```data class```.
- **Store unique and unordered values**: In this scenario, consider using a ```set``` or ```dictionary```. Sets don’t allow duplicated values, and dictionaries can’t hold duplicated keys. Run many membership tests where item doesn’t matter: In this case, consider using a set. Sets are optimized for this type of operation.
- **Run advanced array and matrix operations**: In these situations, consider using ```NumPy’s``` specialized data structures.
- **Manipulate your data as a stack or queue**: In those cases, consider using ```deque``` from the collections module or ```Queue```, ```LifoQueue```, or ```PriorityQueue```. These data types are thread-safe and optimized for fast inserting and removing on both ends.

Depending on your specific scenario, lists may or may not be the right tool for the job. Therefore, you must carefully evaluate your needs and consider advanced data structures like the ones listed above.


## Conclusion
In the default implementation of Python, called CPython, lists are represented as an **array of objects in memory**. Because arrays are stored in sequential, contiguous blocks of memory, they support random access. This means that we can access any element by its index in ```O(1)```, or constant time. C arrays have some fundamental differences from Python lists.

> [!IMPORTANT]
> The important difference for this course is that arrays cannot grow or shrink like a list can. You cannot simply add a new object to the end of an array that is already full. Instead, you have to recreate the entire array, allocating more or less space as needed. This happens behind the scenes so that your Python list can grow or shrink without you—the Python developer—having to worry about memory management.

You never have to think about allocating new space for the array that represents your list. CPython automatically resizes the underlying arrays that make up Python lists when it determines it needs to. When that happens, it typically allocates more space than needed so that the next few append operations on the list don’t require further resizing of the array. In fact, this resizing happens so infrequently that we say the time complexity of an append operation on a list is O(1).

So, that explains why accessing elements in a list and appending new ones is a constant time operation. Where things fall apart is when trying to insert new items into the list anywhere else. If we just insert the new item at the end—aka appending—it’s an ```O(1)``` operation. However, if we need to insert an item somewhere in the middle or at the beginning, it becomes an ```O(n)``` operation where ```n``` is the number of elements in the list.

In other words, the amount of time the operation takes depends on how many elements are in the list. This is because every element after the desired location for the new item must be pushed down by one address to make space for the new one. Then, the new element can be added. As you can imagine, the slowest scenario is inserting a new item at the beginning of a list, which requires that all the existing elements in the underlying array be shifted down by one address.

In addition, `sorted` is used to sort the elements of a list in ascending order which has the time complexity of `n*log(n)`; where `n` is the number of elements in the list.

> [!WARNING]
> The bottom line is this: ***lists are great when we need to quickly obtain items at a specific index or when we need to append new items to the end, but they start to slow down when we try to insert new items somewhere in the middle or—in the worst case—at the beginning.*** 