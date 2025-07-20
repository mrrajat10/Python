class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price


order1 = Order("Log", 10000)
order2 = Order("abs", 32342)
print(order1 > order2)
