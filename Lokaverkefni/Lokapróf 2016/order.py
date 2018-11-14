"""
EKKI HÆGT AÐ GERA ÞETTA VERKEFNI VEGA ÞESS AÐ ÞAÐ ÞARF AÐ NOTA VEKTORA!!!

SKOÐA MÖGULEGA SEM SEINASTA VERKEFNI
"""


class Order(object):
    def __init__(self, name="", price=0, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def addLine(self):
        pass

    def getTotal(self):
        pass

    def __str__(self):
        return


class OrderLine(object):
    def __init__(self):
        pass

    def __str__(self):
        return


def main():
    order = Order()
    # // The customer is buying 12 eggs at 60 kr. each.
    # // There is no discount on eggs (in this case).
    order.addLine("eggs", 60, 12, 0)
    # // The customer buys a single bread, the price of the bread
    # // is 200 but we give the customer a 10% discount.
    order.addLine("bread", 200, 1, 10)
    # // The customer buys 2 cartons of milk, the price of each carton is
    # 120 kr., and we then give the customer a 5% discount.
    order.addLine("milk", 120, 2, 5)
    total = 0
    totalExcludingDiscount = 0
    discount = 0
    order.getTotal(total, totalExcludingDiscount, discount)
    print("The total price is:", total)
    print(order)
    return 0
