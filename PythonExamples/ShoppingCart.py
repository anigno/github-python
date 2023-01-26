class ShippingCart:
    def __init__(self):
        self.items = []

    def addItem(self, name, price):
        item = (name, price)
        self.items.append(item)

    def __iter__(self):
        return self.items.__iter__()

    def TotalPrice(self):
        total=0
        for i in self.items:
            total+=i[1]
        return total


cart = ShippingCart()
cart.addItem('car', 20000)
cart.addItem('tv', 500)

for t in cart:
    print(t)

print("Total price {0}$".format(cart.TotalPrice()))


