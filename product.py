class Product(object):
    def __init__(self, item, weight, brand, cost, status):
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
        return self
    def sell(self):
        self.status = "Sold!"
        return self
    def tax(self, float):
        total = self.cost + (float * self.cost)
        print "Your total with the tax is ${}".format(total)
        return self
    def Return(self):
        reason = ("> ")
        if "defective" in reason:
            self.status = "Defective"
            self.cost = 0
            print self
        elif "box" in reason:
            self.status = "Like New, For Sale"
            print self
        elif "open" in reason:
            self.status = "Used"
            self.cost = self.cost - (self.cost * .20)
            print self
        return self

    def displayInfo(self):
        print "Your item is {} {}".format(self.brand, self.item)
        print "Weight: {} ".format(self.weight)
        print "Total Cost: {} ".format(self.cost)
        print "This item is {} ".format(self.status)
        return self

tennis_Shoes = Product("Tennis Shoes", 1, "Nike", 99.99, "For Sale")
tennis_Shoes.Return().displayInfo()
