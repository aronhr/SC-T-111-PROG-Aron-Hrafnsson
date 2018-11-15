class Vehicle(object):
    def __init__(self, license="", year=0, weight=0.00, fee=0.00):
        self.license = license
        self.year = year
        self.weight = weight
        self.fee = fee

    def get_license(self):
        return self.license

    def get_year(self):
        return self.year

    def get_weight(self):
        return self.weight

    def get_fee(self):
        return self.fee

    def set_weight(self, other):
        self.weight = other

    def set_fee(self, other):
        self.fee = other

    def __str__(self):
        return "Vehicle: {} {} Weight={} Fee=${}".format(self.get_license(), self.get_year(), self.get_weight(), self.get_fee())


class Car(Vehicle):
    def __init__(self, license="", year=0, style=""):
        self.__style = style
        Vehicle.__init__(self, license, year)

    def get_style(self):
        return self.__style

    def set_weight(self, weight):
        self.weight = weight
        if weight < 3000:
            self.fee = 30
        elif 3000 <= weight < 5000:
            self.fee = 40
        else:
            self.fee = 50

    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.get_license(), self.get_year(), self.get_style(), self.get_weight(), self.get_fee())


class Truck(Vehicle):
    def __init__(self, license="", year=0, wheels=0):
        Vehicle.__init__(self, license, year)
        self.__wheels = wheels

    def set_weight(self, weight):
        self.weight = weight
        if weight < 3000:
            self.fee = 40
        elif 3000 <= weight < 5000:
            self.fee = 50
        elif 5000 <= weight < 10000:
            self.fee = 60
        else:
            self.fee = 70

    def get_wheels(self):
        return self.__wheels

    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.get_license(), self.get_year(), self.get_wheels(), self.get_weight(), self.get_fee())


class Motorbike(Vehicle):
    def __init__(self, license="", year=0, CC=0):
        Vehicle.__init__(self, license, year)
        self.__CC = CC

    def get_CC(self):
        return self.__CC

    def set_CC(self, other):
        self.__CC = other
        if other < 50:
            self.fee = 10
        elif 50 <= other < 200:
            self.fee = 20
        else:
            self.fee = 35

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.get_license(), self.get_year(), self.get_CC(), self.get_fee())


def main():
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)
    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight()))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee()))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC()))
    print()
    # Put the four vehicles into a list.
    # Then loop through the list and call the print function for each of the
    # vehicles.
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE

    vehicle_list = [v1, c1, t1, b1]
    for x in vehicle_list:
        print(x)

    v1 = c1
    print(v1)
    print()


main()
