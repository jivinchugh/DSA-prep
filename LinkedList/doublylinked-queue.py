class StackDoublyLinkedList:

    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.top = None  # Points to the top element of the stack

    # Push an element onto the stack
    def push(self, data):
        new_node = self.Node(data, next=self.top)
        if self.top is not None:
            self.top.prev = new_node  # Update the previous top node's previous link
        self.top = new_node  # Update the top to the new node

    # Pop an element from the stack
    def pop(self):
        if self.top is None:
            raise IndexError("pop() from an empty stack")
        removed_data = self.top.data
        self.top = self.top.next  # Move the top pointer to the next node
        if self.top is not None:
            self.top.prev = None  # Update the new top's previous link
        return removed_data

    # Peek at the top element without removing it
    def peek(self):
        if self.top is None:
            raise IndexError("peek() from an empty stack")
        return self.top.data

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Traverse the stack (print all elements)
    def traverse(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicates the end of the stack
