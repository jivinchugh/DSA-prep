'''A self adjusting linked list is a linked list where a successful search causes the list to adjust so that the found item is moved to the front (and thus allowing successive search for same item to be more readily found).

Given the following class declarations for a doubly linked self adjusting linked list:

class SelfAdjustingList:
	class Node:
		def __init__(self, dat, nx, pr):
			self.data = dat
			self.next = nx
			self.prev = pr

	def __init__(self, id_list):
                self.front = ...
                self.back = ...
Write the following function:

def search(self, v)
This function searches for v within the list and returns true if v is found. If not found, function returns false
The list will be adjusted so that the found node is moved so that it becomes the first data node in the list
Function must have run time of O(n)
Implement two versions of this, one using sentinels and one without.'''

class SelfAdjustingList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self, id_list):
        self.front = None
        self.back = None

        # Initialize the list by adding each item from id_list
        for item in id_list:
            self.push_back(item)

    def push_back(self, data):
        new_node = self.Node(data)
        if not self.back:
            # If the list is empty, both front and back point to the new node
            self.front = new_node
            self.back = new_node
        else:
            # Add new node at the back and update pointers
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node

    def search(self, v):
        # Start from the front of the list
        current = self.front
        
        while current is not None:
            if current.data == v:
                # Move the node to the front if found

                # If already at the front, no need to adjust
                if current == self.front:
                    return True
                
                # Detach the node from its current position
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

                # If the current node is at the back, update the back pointer
                if current == self.back:
                    self.back = current.prev

                # Insert the node at the front
                current.next = self.front
                current.prev = None
                self.front.prev = current
                self.front = current

                return True

            current = current.next
        
        # If v is not found, return False
        return False

# Example usage without sentinels
linked_list = SelfAdjustingList([3, 8, 1, 6, 9])
print("WITHOUT SENTINELS")
print(linked_list.search(6))  # True, should move '6' to front
print(linked_list.search(3))  # True, should move '3' to front
print(linked_list.search(10))  # False, not found


class SelfAdjustingListWithSentinels:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self, id_list):
        # Create sentinel nodes for front and back
        self.front = self.Node()  # Front sentinel (dummy)
        self.back = self.Node()   # Back sentinel (dummy)

        # Link the front and back sentinels
        self.front.next = self.back
        self.back.prev = self.front

        # Initialize the list by adding each item from id_list
        for item in id_list:
            self.push_back(item)

    def push_back(self, data):
        # Create a new node
        new_node = self.Node(data)

        # Insert it before the back sentinel
        new_node.prev = self.back.prev
        new_node.next = self.back

        self.back.prev.next = new_node
        self.back.prev = new_node

    def search(self, v):
        # Start from the first real node (after front sentinel)
        current = self.front.next

        while current != self.back:  # Stop at the back sentinel
            if current.data == v:
                # Move the node to the front if found

                # If already at the front (after the sentinel), no need to adjust
                if current.prev == self.front:
                    return True

                # Detach the node from its current position
                current.prev.next = current.next
                current.next.prev = current.prev

                # Insert the node right after the front sentinel
                current.next = self.front.next
                current.prev = self.front
                self.front.next.prev = current
                self.front.next = current

                return True

            current = current.next
        
        # If v is not found, return False
        return False

# Example usage with sentinels
linked_list_sentinels = SelfAdjustingListWithSentinels([3, 8, 1, 6, 9])
print("\nWITH SENTINELS")
print(linked_list_sentinels.search(6))  # True, should move '6' to front
print(linked_list_sentinels.search(3))  # True, should move '3' to front
print(linked_list_sentinels.search(10))  # False, not found
