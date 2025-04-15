# Problem: Create a class order which stores item and its prices. Use Dunder function __gt__() to convey that: order1 > order2 if price of order1 > price of order2

class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def showorder(self):
        print(self.item, self.price)

    def __gt__(self, other):
        return self.price > other.price
        
a = order('pen', 10)
b = order('pencil', 5)
c = order('ruler', 10)
print(a>b)
