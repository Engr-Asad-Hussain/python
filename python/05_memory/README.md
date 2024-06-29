## Stack Memory
1. **Definition**: The stack is a region of memory that stores temporary variables created by each function (including the main function). It operates in a last-in, first-out (LIFO) manner.
2. **Characteristics**:
  - **Automatic Allocation**: Memory is automatically allocated and deallocated by the system when functions are called and return.
  - **Fast Access**: Accessing variables on the stack is very fast because it uses CPU registers.
  - **Limited Size**: The size of the stack is limited and defined by the system. It can easily overflow if too many nested functions or very large local variables are used (stack overflow).
  - **Scope and Lifetime**: Variables on the stack are only accessible within the function they are defined and are destroyed once the function exits.

## Heap Memory
1. **Definition**: The heap is a region of memory used for dynamic memory allocation where variables are allocated and freed by the programmer.
2. **Characteristics**:
  - **Manual Allocation**: Memory must be manually allocated and deallocated by the programmer using functions like `malloc`, `free` in C, or `new`, `delete` in C++.
  - **Slower Access**: Accessing variables on the heap is slower compared to the stack because it requires pointer dereferencing.
  - **Unlimited Size**: The heap size is typically larger than the stack and can grow as needed (limited by the system's memory).
  - **Scope and Lifetime**: Variables on the heap remain in memory until they are explicitly deallocated by the programmer or the program ends.

## Heap and Stack in Python and C
### Python
- **Stack Memory**: Python uses the stack to manage function calls and local variables. Each function call creates a new stack frame, and the local variables are stored within these frames.
- **Heap Memory**: Python objects (including data structures like `lists`, `dictionaries`, etc.) are allocated on the heap. Python's memory management, including ***garbage collection***, takes care of allocating and deallocating memory on the heap, which simplifies memory management for the programmer.
### C
- **Stack Memory**: In C, local variables and function call information (like `return addresses`) are stored on the stack. The programmer does not explicitly manage the stack; the compiler and runtime handle it.
- **Heap Memory**: C provides functions like `malloc`, `calloc`, `realloc`, and `free` for dynamic memory allocation on the heap. The programmer is responsible for managing the memory, including freeing it to avoid memory leaks.

## Example Stack-C
Consider the following C code:
```c
#include <stdio.h>

void funcA() {
    int a = 10;  // Local variable stored on the stack
    int b = 20;  // Local variable stored on the stack
    printf("a: %d, b: %d\n", a, b);
}

void funcB() {
    int c = 30;  // Local variable stored on the stack
    funcA();
    printf("c: %d\n", c);
}

int main() {
    funcB();
    return 0;
}
```
1. `main` function starts and calls `funcB`.
2. `funcB` allocates memory for `c` on the stack and calls `funcA`.
3. `funcA` allocates memory for `a` and `b` on the stack.
4. When `funcA` completes, it returns control to `funcB`, and the memory for `a` and `b` is deallocated.
5. `funcB` completes, and the memory for `c` is deallocated.

## Example Heap-C
Consider the following C code:
```c
#include <stdio.h>
#include <stdlib.h>

void func() {
    int *p = (int*)malloc(3 * sizeof(int));  // Allocate memory on the heap
    if (p == NULL) {
        printf("Memory allocation failed\n");
        return;
    }
    p[0] = 10;
    p[1] = 20;
    p[2] = 30;
    printf("p[0]: %d, p[1]: %d, p[2]: %d\n", p[0], p[1], p[2]);
    free(p);  // Free heap memory
}

int main() {
    func();
    return 0;
}
```
1. `main` function calls `func`.
2. `func` allocates memory for an array of 3 integers on the heap.
3. Values 10, 20, and 30 are stored in the heap memory pointed to by `p`.
4. `func` completes and frees the allocated heap memory.

## Example Stack and Heap in Python
In Python, the stack is used for function calls and local variables within those functions.
```py
def funcA():
    a = 10  # Local variable on the stack
    b = 20  # Local variable on the stack
    print(f"a: {a}, b: {b}")

def funcB():
    c = 30  # Local variable on the stack
    funcA()
    print(f"c: {c}")

funcB()
```

Python objects, including `lists`, `dictionaries`, and custom `objects`, are stored on the heap. The Python interpreter manages heap memory using `garbage collection`.
```py
def func():
    lst = [10, 20, 30]  # List allocated on the heap
    print(lst)

func()
```
In Python, the list lst is stored on the heap, but the reference to it is on the stack. When func completes, the reference is removed, and the garbage collector will eventually free the heap memory.

## Walkthrough by ArjanCodes
The Stack is a basic model of memory that operates, name already says it, as a Stack. You allocate memory by `pushing` something onto the stack, and when you no longer need the memory, you `pop` it from the stack again.

Assume this is a stack of a program, in that program lets create a variable and assign a value to it. In order to do that you need to allocate memory first. Now, lets say you call a function that also requires memory, because you are going to need to store metadata of a function, such as function name, arguments. Now lets say that in the function, you declare another variable. The function does some work and then it completes. Now, you can pop the allocated memory again from the stack and continue your program afterwards.

Well, there is a small problem. When you allocate memory on the stack, you need to specify how much. That way, you can reserve that memory space and it will still be available after something else is put top of it. But that's not always possible. For example, lets say you want to store the name of a user that user provides in a text field. You don't know how many characters your user is going to type, so how much space you actually need? Now, because the stack only has push and pop operations, you can't change the size of the memory (or a variable you define). This is a problem, you could reseve a ton of space? Just in case the user's parents decide to name their child after the chemical composition of titin. But this wouldn't be very efficient. You would require a lot of memory and you would still have no guarantee that you wouldn't run into problems when a value needs more space than you thought. And if continue adding a lot of memory you are going to get a stack overflow.

To really solve this problem you need a different memory model, and that's called the Heap. What is Heap? The heap is a space where you can freely allocate memory. Since allocating the memory on heap happens separately for each things that you need to store, you don't have a space problem that you have seen on the stack. If you don't have enough space you just allocate more memory to a variable. There is not the limitation that the stack has that you can only put things on top of each other. With the stack, it is easy refer to a memory because you know exactly where is what. And also it is easy to deallocate the memory because as soon as a stack frame is popped, everything is cleaned up. For the heap this doesn't work because memory allocation is not linked to any scope like with the stack. So lets first solve how you can refer to this memory on the heap and this is done with a concept called pointer. A pointer is nothing more than a variable that contains a memory address. Consider a variable that contains a memory address (pointer) stored in a stack and we let it point to a value which is stored in a heap. You can access the memory that the pointer points to by referencing it. What happens if the function call get out of the scope? The pointer simply removes from the stack but the memory on the stack is still allocated. There is now no longer a variable that contains the memory address of value on the heap. In other words, you no longer have a way to refer to this memory. That does not have to be a problem if you no longer need the data in your program but it does need to be cleaned up. Some languages like `Java`, `Python`, `C Sharp` have a automatic garbage collector that every once in a while looks through memory and checks what memory can be freed up by looking at whether something is still referring to that memory. This garbage collector is directly handled by the developer who is responsible to cleanup the unused memory. This is what `C` and `C++` does. The problem is that developers than have to make sure to deallocate memory they no longer need. However, developers are forgetful. When memory is not deallocated and there is no way to refer to it anymore that's we call a memory leak. The memory management in Python is very simple, Python does not wnat you to think about whether to use the stack or the heap or having to cleanup the memory. Python is optimized for making things very simple for developers. But its also a significant reason for Python being slow. I think this is a reasonable trade-off. Yes Python is slow but simplicity is also what led to widespread adoption of Python in many domains. And lets be honest here. In most cases, performance is not the deciding factor for picking a progamming language. Instead, most people look at ease of use, the ecosystem, libraries and other tools that available. 

So whenever someone tell you that Python is a toy language and you should use a real language like `C` or `Rust` tell them you prefer quick development and iteration over code that may be performant but also much harder to write.

## Summary
- **Stack Memory**: Used for static memory allocation (local variables, function calls), automatically managed, limited in size, fast access.
- **Heap Memory**: Used for dynamic memory allocation, manually managed (or garbage collected in languages like Python), larger and flexible, slower access.

## References
- https://www.youtube.com/watch?v=6jgu9tmbrrE
- https://www.geeksforgeeks.org/stack-vs-heap-memory-allocation/
