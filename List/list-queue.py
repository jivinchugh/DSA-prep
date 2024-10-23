class QueueList:
    
    # Queue constructor
    def __init__(self):
        self.queue = []  # Use Python's built-in list

    # Enqueue (add) an element to the rear of the queue
    def enqueue(self, data):
        self.queue.append(data)  # Add to the end of the list (rear)

    # Dequeue (remove) an element from the front of the queue
    def dequeue(self):
        if not self.queue:
            raise IndexError("dequeue() used on empty queue")
        return self.queue.pop(0)  # Remove and return the first element (front)

    # Peek at the front element without removing it
    def peek(self):
        if not self.queue:
            raise IndexError("peek() used on empty queue")
        return self.queue[0]  # Return the first element (front)

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Traverse the queue (print all elements)
    def traverse(self):
        for item in self.queue:
            print(item, end=" -> ")
        print("None")  # Indicates the end of the queue

queue_list = QueueList()
queue_list.enqueue(10)
queue_list.enqueue(20)
queue_list.enqueue(30)

queue_list.traverse()  # Output: 10 -> 20 -> 30 -> None

print(queue_list.dequeue())  # Output: 10
queue_list.traverse()        # Output: 20 -> 30 -> None

print(queue_list.peek())     # Output: 20
print(queue_list.is_empty()) # Output: False
