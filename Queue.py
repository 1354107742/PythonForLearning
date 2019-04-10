#链表方式
#初始化一个空队列
class LinkedQueue(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0
		
		
#入队操作
	def enqueue(self,value):
		new_node = Node(value)
		
		if self.tail is not None:
			self.tail.next = new_node
			
		else:
			self.head = new_node
		
		self.tail = new_node
		self.count += 1
		
		
#出队操作
	def dequeue(self):
		if not self.is_empty():
			#给 node赋予头部
			tmp = self.head
			self.head = self.head.next
			print("dequeue success")
			self.count -= 1
			return tmp
		else:
			raise ValueError("warning")

#验空			
	def is_empty(self):
		if self.head is None and self.tail is None:
			return True
		else:
			return False
	
#返回头部值
	def peek(self):
		return self.head.data

		
#返回队列长度
	def __len__(self):
		return self.count

		
		
#返回空队
	def is_empty(self):
		return self.count == 0

		
#数值输出操作		
	def print(self):
		node = self.head
		while node:
			print(node.value,end = "")
			node = self.node.next
		print('')
