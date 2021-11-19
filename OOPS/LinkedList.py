class LinkedList:
	class Node:
		def __init__(self,val,node):
			self.val = val
			self.next = node

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def insertAtStart(self,val):
		temp = self.Node(val,self.head)
		self.head = temp 
		if(self.tail==None):
			self.tail = temp
		self.size+=1

	def insertAtEnd(self,val):
		if(self.tail==None):
			insertAtStart(val)
		else:
			temp = self.Node(val,None)
			self.tail.next = temp
			self.tail = temp
			self.size+=1

	def insertAtIndex(self,val,index):
		if(index==0):
			self.insertAtStart(val)
		elif(index<0 or index>self.size):
			raise Exception('Index out of range')
		elif(index==self.size):
			self.insertAtEnd(val)
		else:
			temp = self.head

			for i in range(1,index):
				temp = temp.next
			newNode = self.Node(val,temp.next)
			temp.next = newNode
			self.size+=1

	def deleteFirst(self):
		if(self.head!=None):
			self.head = self.head.next
			self.size-=1
		else:
			raise Exception('Linked List is empty!')
	
	def deleteLast(self):
		if(self.tail!=None):
			self.deleteAtIndex(self.size-1)
		else:
			raise Exception('Linked List is empty!')

	
	def deleteAtIndex(self,index):
		if(index<0 or index>=self.size):
			raise Exception('Index out bound!')
		elif(index==0):
			self.deleteFirst()
		else:
			temp = self.head
			prev = None
			for i in range(1,index+1):
				prev = temp
				temp = temp.next
			prev.next = temp.next
			self.size-=1

	def display(self):
		temp = self.head
		while(temp!=None):
			print(str(temp.val)+'->',end='')
			temp = temp.next

		print('END')
	

ll = LinkedList()
ll.insertAtStart(20)
ll.insertAtStart(80)
ll.insertAtStart(30)
ll.insertAtStart(230)
ll.insertAtStart(320)
ll.insertAtStart(90)
ll.insertAtEnd(100)
ll.insertAtEnd(1000)
ll.insertAtStart(50)
ll.insertAtIndex(2,4)
ll.display()
ll.insertAtIndex(99,5)
ll.display()
ll.deleteAtIndex(3)
ll.display()
ll.deleteLast()
ll.deleteLast()
ll.deleteLast()
ll.display()