class SinglyLinked:
    
    # Inner Node class
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

    # Singly Linked List constructor
    def __init__(self):
        self.front = None  # Points to the first node

    # Get the front node
    def get_front(self):
        return self.front

    ### Insert Functions ###

    # Insert at the front
    def push_front(self, data):
        newnode = self.Node(data, next=self.front)
        self.front = newnode

    # Insert at the back
    def push_back(self, data):
        newnode = self.Node(data)
        if self.front is None:  # If the list is empty
            self.front = newnode
        else:
            current = self.front
            while current.get_next():
                current = current.get_next()
            current.next = newnode

    ### Delete Functions ###

    # Remove the front element
    def pop_front(self):
        if self.front is None:
            raise IndexError("pop_front() used on empty list")
        else:
            remove = self.front
            removed_data = remove.get_data()
            self.front = self.front.get_next()
            del remove
            return removed_data

    # Remove the back element
    def pop_back(self):
        if self.front is None:
            raise IndexError("pop_back() used on empty list")
        elif self.front.get_next() is None:  # Only one element
            remove = self.front
            removed_data = remove.get_data()
            self.front = None
            del remove
            return removed_data
        else:
            current = self.front
            prev = None
            while current.get_next():  # Traverse to the last node
                prev = current
                current = current.get_next()
            removed_data = current.get_data()
            prev.next = None  # Remove the last node
            del current
            return removed_data

    ### Search Function ###

    # Search for a value and return True if found
    def search_value(self, value):
        current = self.front
        while current:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False

    ### Traverse Function ###

    # Print all elements in the list
    def traverse(self):
        current = self.front
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")  # Indicates the end of the list


sll = SinglyLinked()

# Insert at front and back
sll.push_front(10)
sll.push_back(20)
sll.push_back(30)

# Traverse the list
sll.traverse()  # Output: 10 -> 20 -> 30 -> None

# Pop front
sll.pop_front()  # Removes 10
sll.traverse()   # Output: 20 -> 30 -> None

# Pop back
sll.pop_back()   # Removes 30
sll.traverse()   # Output: 20 -> None

# Search for value
print(sll.search_value(20))  # Output: True
print(sll.search_value(40))  # Output: False
