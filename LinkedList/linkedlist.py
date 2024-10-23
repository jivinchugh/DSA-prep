class DoublyLinked:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self, data = None):
		self.front = None
		self.back = None

	def get_front(self):
		return self.front

	def get_back(self):
		return self.back

	def push_front(self, data):
		newnode = self.Node(data, next = self.front)
		if self.front is None:
			self.back = newnode
		else:
			self.front.prev = newnode
		self.front = newnode


	def push_back(self,data):
		newnode = self.Node(data, prev = self.back)
		if self.back is None:
			self.front = newnode
		else:
			self.back.next = newnode
		self.back = newnode

	def pop_front(self):
		if self.front is None:
			raise IndexError("pop_front() used on empty list")
		else:
			remove = self.front
			removed_data = remove.get_data()
			self.front = self.front.next
			if self.front:
				self.front.prev = None
			else:
				self.back = None
			del remove
			return removed_data

	def pop_back(self):
		if self.back is None:
			raise IndexError("pop_back() used on empty list")
		else:
			remove = self.back
			removed_data = remove.get_data()
			self.back = self.back.prev
			if self.back:
				self.back.next = None
			else:
				self.front = None
			del remove
			return removed_data


class Sentinel:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self, data = None):
		self.front = self.Node(None, None, None)
		self.back = self.Node(None, None, self.front)
		self.front.next = self.back

	def get_front(self):
		if self.front.next == self.back:
			return None
		else:
			return self.front.next

	def get_back(self):
		if self.back.prev == self.front:
			return None
		else:
			return self.back.prev

	def push_front(self, data):
		newnode = self.Node(data, self.front.next, self.front)
		self.front.next.prev = newnode
		self.front.next = newnode

	def push_back(self, data):
		newnode = self.Node(data, self.back, self.back.prev)
		self.back.prev.next = newnode
		self.back.prev = newnode

	def pop_front(self):
		if self.front.next == self.back:
			raise IndexError("pop_front() used on empty list")
		else:
			remove = self.front.next
			removed_data = remove.get_data()
			self.front.next = remove.next
			remove.next.prev = self.front
			del remove 
			return removed_data


	def pop_back(self):
		if self.back.prev == self.front:
			raise IndexError("pop_back() used on empty list")
		else:
			remove = self.back.prev
			removed_data = remove.get_data()
			self.back.prev = remove.prev
			remove.prev.next = self.back
			del remove
			return removed_data





