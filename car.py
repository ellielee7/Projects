class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel
        self.price = price
        if self.price >= 10000:
            print "Tax: 0.15"
        else:
            print "Tax: 0.12"



    def display_all(self):
        print 'Price: ${}'.format(self.price)
    	print 'Speed: ' + str(self.speed) + 'mph'
    	print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Fuel: ' + str(self.fuel)
        print "-" * 17
        return self

car1 = Car(150000, 35, 'Full', 95)
car1.display_all()
car2 = Car(9000, 40, 'Empty', 45)
car2.display_all()
car3 = Car(150000, 25, 'Almost Empty', 55)
car3.display_all()
car4 = Car(4000, 75, 'Almost Full', 35)
car4.display_all()
car5 = Car(12000, 30, 'Full', 25)
car5.display_all()
