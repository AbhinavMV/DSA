class DLL:
	class Node:
		def __init__(self,val,next=None,prev=None):
			self.val = val
			self.next = next
			self.prev = prev
	
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def insertAtStart(self,val):
		temp = self.Node(val,self.head)
		if(self.tail==None):
			self.tail = temp
		if(self.head!=None):
			self.head.prev = temp
		self.head = temp
		self.size+=1

	def insertAtEnd(self,val):
		temp = self.Node(val,None,self.tail)
		if(self.tail!=None):
			self.tail.next = temp
		if(self.head==None):
			self.head = temp
		self.tail = temp
		self.size+=1

	def insertAtIndex(self,val,index):
		if(index==0):
			self.insertAtStart(val)
		elif(index<0 or index>self.size):
			raise Exception("Index out of bound!")
		elif(index==self.size):
			self.insertAtEnd(val)
		else:
			temp = self.Node(val)
			previous = None
			current = self.head
			for i in range(0,index):
				previous = current
				current=current.next
			temp.next = previous.next
			previous.next = temp
			temp.prev = previous
			current.prev = temp
			self.size += 1

	def deleteFirst(self):
		if(self.size==0):
			raise Exception("List is Empty!")
		elif(self.size == 1):
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next
			self.head.prev = None
			self.size-=1

	def deleteLast(self):
		if(self.size==0):
			raise Exception("List is Empty!")
		elif(self.size == 1):
			self.head = None
			self.tail = None
		else:
			self.tail = self.tail.prev
			self.tail.next = None
			self.size -= 1

	def deleteAtIndex(self,index):
		if(self.size==0):
			raise Exception("List is Empty!")
		elif(index<0 or index>=self.size):
			raise Exception("Index out of bound!")
		elif(index==0):
			self.deleteFirst()
		elif(index==self.size-1):
			self.deleteLast()
		else:
			temp = self.head
			for i in range(index):
				temp = temp.next
			print(temp.val)
			temp.next.prev = temp.prev
			temp.prev.next = temp.next
			self.size -= 1

	def display(self):
		temp = self.head
		while(temp!=None):
			print(str(temp.val)+'->',end='')
			temp = temp.next
		print('END')

dll = DLL()
dll.insertAtIndex(1,0)
dll.insertAtIndex(2,1)
dll.insertAtStart(90)
dll.insertAtStart(50)
dll.insertAtStart(20)
dll.insertAtEnd(120)
dll.insertAtEnd(130)
dll.insertAtEnd(10)
dll.insertAtIndex(230,1)
dll.display()
dll.deleteFirst()
dll.deleteLast()
dll.display()
dll.deleteAtIndex(3)
dll.display()