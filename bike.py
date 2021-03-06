class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: $' + str(self.price)
		print 'Speed: ' + str(self.max_speed) + 'mph'
		print 'Miles: ' + str(self.miles) + 'miles'
		return self
	def ride(self):
		print 'Riding'
		self.miles += 10
		return self
	def reverse(self):
		print 'Reversing'
		self.miles -= 5
		return self

bike1=Bike(50.95, 12)
bike1.ride().ride().ride().reverse().displayInfo()

bike2=Bike(75.95, 20)
bike2.ride().ride().reverse().reverse().displayInfo()
