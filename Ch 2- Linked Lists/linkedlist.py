# Cracking the Coding Interview Chapter 2 Linked List

# Nodes and different types of linked lists

class Node:
    def __init__(self, data):
        self.value = value
        self.next = None        # Next Pointer
        self.previous = None    # Previous Pointer


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_data):
        """
        Push new data at the start of the linked list
        and change head to the new node
        """
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head

            self.head = new_node

        return
