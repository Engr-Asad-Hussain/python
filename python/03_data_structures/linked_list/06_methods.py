class Node:
    def __init__(self, value: int, next: "Node" = None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head: Node | None = None) -> None:
        self.head = head

    def insert_at_begining(self, new_node: Node) -> None:
        # 1. keep track of the old head
        old_head = self.head
        # 2. assign new node to the head
        self.head = new_node
        # 3. make sure new head.next references the old head
        new_node.next = old_head
    
    def insert_at_end(self, new_node: Node) -> None:
        # assuming no elements in the Linked List
        if self.head is None:
            self.head = new_node
            return
        
        # assuming some elements are present in the Linked List
        node = self.head
        while True:
            if node.next is None:
                node.next = new_node
                return
            node = node.next
    
    def remove_at_begining(self) -> None:
        if self.head is None:
            raise IndexError('Linked List is empty')
        
        # 1. keep the track of old head
        old_head = self.head
        # 2. adjust the head to point to the next of head
        self.head = old_head.next

    def remove_at_end(self) -> None:
        if self.head is None:
            raise IndexError('Linked List is empty')
        
        # 1. assign previous node as current head node
        previous_node = self.head
        # 2. run the loop till node.next.next node points to None
        while previous_node.next.next is not None:
            previous_node = previous_node.next
        
        # 3. modify node.next as None; hence we removed .next which is the last node
        previous_node.next = None


    def traverse(self):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

# 1. initiate empty linked list
llist = LinkedList()

# 2. creating nodes and chaining them together
node1 = Node(value=1)
llist.head = node1

node2 = Node(value=5)
node1.next = node2

node3 = Node(value=8)
node2.next = node3

# insert at the begining
# llist.insert_at_begining(new_node=Node(10))

# # # insert at the end
# llist.insert_at_end(new_node=Node(0))

# # remove from the begining
# llist.remove_at_begining()

# remove from the end
# llist.remove_at_end()

# traverse the linked list
llist.traverse()

# 3. demonstrate chain
node = llist.head
while node is not None:
    print(" ", node.value)
    node = node.next