from copy import deepcopy
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional[Any] = None) -> None:
        """
        Initialize a Node in a linked list.\n
        Args:
            - data (Any): The data value to store in the node.
            - next (Optional[Any], None): The reference to the next node. Defaults to None.
        """

        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self, nodes: list[Any] | None = None) -> None:
        """
        Initialize a linked list with optional initial nodes.\n
        Args:
            - nodes (list[Any] | None): List of initial node data. Defaults to None.\n
        Example:\n
        >>> linked_list = LinkedList()
        >>> print(linked_list)
        None

        >>> linked_list = LinkedList(['A', 'B', 'C'])
        >>> print(linked_list)
        A -> B -> C -> None
        """

        self.head: Optional[Node] = None
        if nodes is not None and isinstance(nodes, list):
            previous_node: Optional[Node] = None
            for element in nodes:
                node = Node(element)
                if previous_node is None:
                    self.head = node
                else:
                    previous_node.next = node
                previous_node = node

    def __repr__(self) -> str:
        """
        Return the string representation of all the nodes in the linked list.\n
        It appends all the nodes in the linked list and return the string representation at the end.
        """

        node = self.head
        nodes: list[str] = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        One of the most common things you will do with a linked list is to `traverse` it.
        Traversing means going through every single node, starting with the head of the linked list
        and ending on the node that has a next value of `None`.\n
        Traversing is just a fancier way to say `iterating`. So, with that in mind,
        create an `__iter__` to add the same behavior to linked lists that you would expect
        from a normal list.
        """

        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append_left(self, element: str):
        """
        Inserting a new node at the beginning of a list is probably the most straightforward
        insertion since you don’t have to traverse the whole list to do it. It’s all about creating
        a new node and then pointing the head of the list to it.\n
        Args:
            - element (str): New element to be inserted at the beginning of the linked list.
        """

        node = Node(element)
        node.next = self.head
        self.head = node

    def append_right(self, element: str):
        """
        Inserting a new node at the end of the list forces you to traverse the whole linked
        list first and to add the new node when you reach the end. You can’t just append to the end
        as you would with a normal list because in a linked list you don’t know which
        node is last.\n
        Args:
            - element (str): New element to be inserted at the ending of the linked list.
        """

        node = self.head
        new_node = Node(element)
        while node is not None:
            if node.next is None:
                node.next = new_node
                return
            node = node.next
        # Else, head is None | Means empty deque
        self.head = new_node

    def pop_left(self):
        """
        Removes and returns the value of the element at the left end of the linked list.\n
        This method removes the first element (leftmost) from the linked list and returns its value.
        The head of the linked list is updated to point to the next element.\n
        Returns:
            Any: The value of the removed element.
        """

        for node in self:
            self.head = node.next
            return node

    def pop_right(self):
        """
        Removes and returns the value of the element at the right end of the linked list.\n
        This method removes the last element (rightmost) from the linked list and returns its value.
        The head of the linked list is updated to point to the next element.\n
        Returns:
            Any: The value of the removed element.
        """

        previous_node = self.head
        for node in self:
            if node.next is None:
                previous_node.next = None
                return node
            previous_node = node

    def reverse(self):
        """
        Reverse all the nodes in the linked list such that the head will be point to the last element
        and the None will be pointing to the first element in the linked list.
        """

        current_node = self.head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node


linked_list = LinkedList()
print(f"{linked_list = } | H={linked_list.head}")

first_node = Node("A")
linked_list.head = first_node
print(f"{linked_list = }| H={linked_list.head}")

second_node = Node("B")
first_node.next = second_node
print(f"{linked_list = }| H={linked_list.head}")

third_node = Node("C")
second_node.next = third_node
print(f"{linked_list = } | H={linked_list.head}")


linked_list = LinkedList(["ABC", "EFG", "PQR"])
print(f"{linked_list = } | H={linked_list.head}")

linked_list.append_left("123")
print(f"{linked_list = } | H={linked_list.head}")

linked_list.append_right("789")
print(f"{linked_list = } | H={linked_list.head}")

linked_list.append_right("KQJ")
print(f"{linked_list = } | H={linked_list.head}")

linked_list.pop_left()
print(f"{linked_list = } | H={linked_list.head}")

linked_list.pop_right()
print(f"{linked_list = } | H={linked_list.head}")

linked_list.reverse()
print(f"{linked_list = } | H={linked_list.head}")


print("... Iterator Method on Linked List ...")
for element in linked_list:
    print(element.data, element.next)
