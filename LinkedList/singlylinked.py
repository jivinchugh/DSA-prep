class SinglyLinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

    def __init__(self):
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def push_front(self, data):
        new_node = self.Node(data, next=self.front)
        if self.front is None:
            self.back = new_node
        self.front = new_node

    def push_back(self, data):
        new_node = self.Node(data)
        if self.back is None:
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def pop_front(self):
        if self.front is None:
            raise IndexError("pop_front() used on empty list")
        else:
            remove = self.front
            removed_data = remove.get_data()
            self.front = self.front.next
            if self.front is None:  # If the list becomes empty
                self.back = None
            del remove
            return removed_data

    def pop_back(self):
        if self.back is None:
            raise IndexError("pop_back() used on empty list")
        else:
            current = self.front
            while current.next != self.back:  # Traverse to the second last node
                current = current.next
            removed_data = self.back.get_data()
            current.next = None  # Remove the last node
            self.back = current
            if self.back is None:  # If the list becomes empty
                self.front = None
            return removed_data

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.get_data())
            current = current.get_next()
        return " -> ".join(map(str, elements))


class Sentinel:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

    def __init__(self):
        self.front = self.Node(None)  # Sentinel front node
        self.back = self.Node(None)    # Sentinel back node
        self.front.next = self.back     # Connect front to back

    def get_front(self):
        if self.front.next == self.back:
            return None
        else:
            return self.front.next

    def get_back(self):
        if self.back.data is None:
            return None
        else:
            current = self.front
            while current.next != self.back:
                current = current.next
            return current

    def push_front(self, data):
        new_node = self.Node(data, self.front.next)
        self.front.next = new_node

    def push_back(self, data):
        new_node = self.Node(data)
        current = self.front
        while current.next != self.back:
            current = current.next
        current.next = new_node
        new_node.next = self.back

    def pop_front(self):
        if self.front.next == self.back:
            raise IndexError("pop_front() used on empty list")
        else:
            remove = self.front.next
            self.front.next = remove.next
            del remove
            return remove.get_data()

    def pop_back(self):
        if self.front.next == self.back:
            raise IndexError("pop_back() used on empty list")
        else:
            current = self.front
            while current.next != self.back:
                current = current.next
            remove = current.next
            current.next = self.back
            del remove
            return remove.get_data()

    def __str__(self):
        elements = []
        current = self.front.next
        while current != self.back:
            elements.append(current.get_data())
            current = current.get_next()
        return " -> ".join(map(str, elements))


# Example Usage
if __name__ == "__main__":
    # Using SinglyLinkedList
    sll = SinglyLinkedList()
    sll.push_front(10)
    sll.push_front(20)
    sll.push_back(30)
    print("Singly Linked List:", sll)
    print("Pop Front:", sll.pop_front())
    print("After Pop Front:", sll)
    print("Pop Back:", sll.pop_back())
    print("After Pop Back:", sll)

    # Using Sentinel
    sentinel_list = Sentinel()
    sentinel_list.push_back(10)
    sentinel_list.push_back(20)
    print("Sentinel Linked List:", sentinel_list)
    print("Pop Front:", sentinel_list.pop_front())
    print("After Pop Front:", sentinel_list)
    print("Pop Back:", sentinel_list.pop_back())
    print("After Pop Back:", sentinel_list)
