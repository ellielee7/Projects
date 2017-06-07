class Product(object):
    def __init__(self, price, item, weight, brand, cost, status):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        return self
    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Item: " + str(self.item)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Total Cost: " + str(self.cost)
        print "This item is " + str(self.status)
        return self

    def changeStatus(self):
        if item == sold:
            self.status = sold
            print "This item is sold"
