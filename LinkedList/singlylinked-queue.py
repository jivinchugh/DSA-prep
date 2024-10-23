class QueueLinkedList:

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

    def __init__(self):
        self.front = None  # Front points to the first element
        self.rear = None   # Rear points to the last element

    # Enqueue (add) an element to the rear of the queue
    def enqueue(self, data):
        newnode = self.Node(data)
        if self.rear is None:  # If queue is empty, both front and rear are the same
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode  # Link the new node to the last node
            self.rear = newnode       # Update the rear to the new node

    # Dequeue (remove) an element from the front of the queue
    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue() used on empty queue")
        remove = self.front
        removed_data = remove.get_data()
        self.front = self.front.get_next()  # Move front to the next node
        if self.front is None:  # If the queue becomes empty, rear should also be None
            self.rear = None
        del remove
        return removed_data

    # Peek at the front element without removing it
    def peek(self):
        if self.front is None:
            raise IndexError("peek() used on empty queue")
        return self.front.get_data()

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Traverse the queue (print all elements)
    def traverse(self):
        current = self.front
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")  # Indicates the end of the queue

queue_ll = QueueLinkedList()
queue_ll.enqueue(10)
queue_ll.enqueue(20)
queue_ll.enqueue(30)

queue_ll.traverse()  # Output: 10 -> 20 -> 30 -> None

print(queue_ll.dequeue())  # Output: 10
queue_ll.traverse()        # Output: 20 -> 30 -> None

print(queue_ll.peek())     # Output: 20
print(queue_ll.is_empty()) # Output: False
