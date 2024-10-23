class StackWithSentinel:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        # Create two sentinel nodes: front (top of the stack) and back (bottom of the stack)
        self.front = self.Node()  # Sentinel node at the front (top)
        self.back = self.Node()   # Sentinel node at the back (bottom)
        self.front.next = self.back
        self.back.prev = self.front

    def is_empty(self):
        return self.front.next == self.back

    def push(self, data):
        new_node = self.Node(data, self.front.next, self.front)
        self.front.next.prev = new_node
        self.front.next = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() used on empty stack")
        remove_node = self.front.next
        self.front.next = remove_node.next
        remove_node.next.prev = self.front
        removed_data = remove_node.data
        del remove_node
        return removed_data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek() used on empty stack")
        return self.front.next.data

    def __iter__(self):
        # Iterator function to iterate through the stack from top to bottom
        current = self.front.next
        while current != self.back:
            yield current.data
            current = current.next

    def __str__(self):
        # Print the stack from top to bottom
        elements = [str(data) for data in self]
        return "Stack (top -> bottom): " + " -> ".join(elements)


# Example Usage
if __name__ == "__main__":
    stack = StackWithSentinel()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack)  # Stack (top -> bottom): 30 -> 20 -> 10
    
    # Iterating over the stack using the built-in iteration function
    for item in stack:
        print(item)  # Outputs: 30, 20, 10

    print("Popped:", stack.pop())  # Popped: 30
    print(stack)  # Stack (top -> bottom): 20 -> 10
    
    for item in stack:
        print(item)  # Outputs: 20, 10
