class Item:
	pay_rate = 0.8 #class attribute
	all = []
	def __init__(self,name:str,price:float,quantity=0): #argument type validations
		#Validations 
		assert price>=0, f'Price {price} is not greater than or equal to zero'
		assert quantity>=0, f'Quantity {quantity} is not greater than or equal to zero'
		
		#Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

		#actions to execute
		Item.all.append(self)

	def calculate_total_price(self):
		return self.price*self.quantity

	def apply_discount(self):
		return self.price * self.pay_rate

	def __repr__(self):
		return f"Item('{self.name}',{self.price})"

item1 = Item('Phone',100,1)
item2 = Item('Laptop',1000,2)

print(Item.all)