from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Any = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def __repr__(self) -> str:
        node = self.head
        nodes: list[str] = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


linked_list = LinkedList()
print("linked_list = [%s]" % linked_list)  # None
print(f"{linked_list.head=}")
print()

first_node = Node("A")
print(f"{first_node.data=}")
print(f"{first_node.next=}")
linked_list.head = first_node
print(f"{linked_list.head=}")
print("linked_list = [%s]" % linked_list)  # A -> None
print()


second_node = Node("B")
print(f"{second_node.data=}")
print(f"{second_node.next=}")
first_node.next = second_node
print(f"{first_node.next=}")
print(f"{linked_list.head=}")
print("linked_list = [%s]" % linked_list)  # A -> B -> None
print()


third_node = Node("C")
print(f"{third_node.data=}")
print(f"{third_node.next=}")
second_node.next = third_node
print(f"{second_node.next=}")
print(f"{linked_list.head=}")
print("linked_list = [%s]" % linked_list)  # A -> B -> C -> None
print()
