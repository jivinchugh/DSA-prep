class QueueDoublyLinkedList:

    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    # Enqueue (add) an element to the rear of the queue
    def enqueue(self, data):
        new_node = self.Node(data)
        if self.rear is None:  # If the queue is empty
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear  # Link the new node to the last node
            self.rear.next = new_node  # Update the last node's next link
            self.rear = new_node  # Move rear to the new node

    # Dequeue (remove) an element from the front of the queue
    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue() from an empty queue")
        removed_data = self.front.data
        self.front = self.front.next  # Move front to the next node
        if self.front is not None:
            self.front.prev = None  # Update the new front's previous link
        else:
            self.rear = None  # If the queue becomes empty, set rear to None
        return removed_data

    # Peek at the front element without removing it
    def peek(self):
        if self.front is None:
            raise IndexError("peek() from an empty queue")
        return self.front.data

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Traverse the queue (print all elements)
    def traverse(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicates the end of the queue
