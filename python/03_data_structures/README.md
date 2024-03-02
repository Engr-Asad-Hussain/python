## Contents
  - [Linked List](#linked-list)
  - [Shallow/Deep copy](#shallow-copy--deep-copy)
  - [List](#lists)
  - [CPython Time Complexities](#python-data-types-time-complexities)


## Linked List
- Linked lists are an ***ordered collection of objects***.
- Linked lists differ from lists in the way that they ***store elements in memory***. While lists use a ***contiguous memory block*** to store references to their data, linked lists store references as part of their own elements.
- In depth discussion present at [data_structures/linked_list/docs.md](https://github.com/Engr-Asad-Hussain/oop/blob/main/data_stuctutres/linked_list/README.md)


## Performance Comparison: Lists vs Linked Lists
- In most programming languages, there are clear differences in the way linked lists and arrays are stored in memory. In Python, however, lists are dynamic arrays. That means that the memory usage of both lists and linked lists is very similar.
- Since the difference in memory usage between lists and linked lists is so insignificant, it’s better if you focus on their performance differences when it comes to ```time complexity```.


### Insertion and Deletion of Elements
- In Python, you can insert elements into a list using ```.insert()``` or ```.append()```. For removing elements from a list, you can use their counterparts: ```.remove()``` and ```.pop()```.
- The main difference between these methods is that you use .insert() and .remove() to insert or remove elements at a specific position in a list, but you use .append() and .pop() only to insert or remove elements at the end of a list.
- Now, something you need to know about Python lists is that inserting or removing elements that are not at the end of the list requires some element shifting in the background, making the operation more complex in terms of time spent.
- With all this in mind, even though inserting elements at the end of a list using .append() or .insert() will have constant time: ***O(1)***, when you try inserting an element closer to or at the beginning of the list, the average time complexity will grow along with the size of the list: ***O(n)***.
- Linked lists, on the other hand, are much more straightforward when it comes to insertion and deletion of elements at the beginning or end of a list, where their time complexity is always constant: ***O(1)***.
- For this reason, linked lists have a performance advantage over normal lists when implementing a queue ***(FIFO)***, in which elements are continuously inserted and removed at the beginning of the list. But they perform similarly to a list when implementing a stack ```(LIFO)```, in which elements are inserted and removed at the end of the list.


### Retrieval of Elements
- When it comes to element lookup, lists perform much better than linked lists. When you know which element you want to access, lists can perform this operation in O(1) time. Trying to do the same with a linked list would take O(n) because you need to traverse the whole list to find the element.
- When searching for a specific element, however, both lists and linked lists perform very similarly, with a time complexity of O(n). In both cases, you need to iterate through the entire list to find the element you’re looking for.


### Conclusion
| Actions | List | Linked List | Faster |
| -------- | :------: | :------: | :------: |
| ```insertion```/```deletion``` at ending | O(1) | O(1) | Same |
| ```insertion```/```deletion``` at beginning | O(n) | O(1) | Linked List |
| ```insertion```/```deletion``` at between | O(n) | O(n) | Same |
| ```retrieval``` of element at specific index | O(1) | O(n) | List |
| ```searching``` of specific element | O(n) | O(n) | Same |

Here, ```n``` is the number of elements in a list or number of nodes in a linked list.


## Shallow copy / Deep copy
Shallow Copy stores the references of objects to the original memory address. Deep copy stores copies of the object's value. Shallow Copy reflects changes made to the new/copied object in the original object. Deep copy doesn't reflect changes made to the new/copied object in the original object.


## Lists
- Python’s list is a flexible, versatile, powerful, and popular built-in data type. 
- It allows you to create variable-length and mutable sequences of objects. 
- In a list, you can store objects of any type. You can also mix objects of different types within the same list, although list elements often share the same type.
- In depth discussion present at [data_structures/list/docs.md](https://github.com/Engr-Asad-Hussain/oop/blob/main/data_stuctutres/list/README.md)


## Python data types time complexities
https://wiki.python.org/moin/TimeComplexity