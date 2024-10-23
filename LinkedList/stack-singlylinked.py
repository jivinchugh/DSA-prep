class StackLinkedList:
    
    # Inner Node class
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

    # Stack constructor
    def __init__(self):
        self.top = None  # Points to the top of the stack

    # Push an element onto the stack
    def push(self, data):
        newnode = self.Node(data, next=self.top)  # Add to the top
        self.top = newnode

    # Pop an element from the stack
    def pop(self):
        if self.top is None:
            raise IndexError("pop() used on empty stack")
        remove = self.top
        self.top = self.top.get_next()
        removed_data = remove.get_data()
        del remove
        return removed_data

    # Peek at the top element without removing it
    def peek(self):
        if self.top is None:
            raise IndexError("peek() used on empty stack")
        return self.top.get_data()

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Traverse the stack (print all elements)
    def traverse(self):
        current = self.top
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")  # Indicates the end of the stack

stack_ll = StackLinkedList()
stack_ll.push(10)
stack_ll.push(20)
stack_ll.push(30)

stack_ll.traverse()  # Output: 30 -> 20 -> 10 -> None

print(stack_ll.pop())  # Output: 30
stack_ll.traverse()    # Output: 20 -> 10 -> None

print(stack_ll.peek()) # Output: 20
print(stack_ll.is_empty()) # Output: False
