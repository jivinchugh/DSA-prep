class StackList:
    
    # Stack constructor
    def __init__(self):
        self.stack = []  # Use Python's built-in list

    # Push an element onto the stack
    def push(self, data):
        self.stack.append(data)  # Append to the end (top of the stack)

    # Pop an element from the stack
    def pop(self):
        if not self.stack:
            raise IndexError("pop() used on empty stack")
        return self.stack.pop()  # Remove and return the top element

    # Peek at the top element without removing it
    def peek(self):
        if not self.stack:
            raise IndexError("peek() used on empty stack")
        return self.stack[-1]  # Return the last element (top of the stack)

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Traverse the stack (print all elements)
    def traverse(self):
        for item in reversed(self.stack):
            print(item, end=" -> ")
        print("None")  # Indicates the end of the stack


stack_list = StackList()
stack_list.push(10)
stack_list.push(20)
stack_list.push(30)

stack_list.traverse()  # Output: 30 -> 20 -> 10 -> None

print(stack_list.pop())  # Output: 30
stack_list.traverse()    # Output: 20 -> 10 -> None

print(stack_list.peek()) # Output: 20
print(stack_list.is_empty()) # Output: False
