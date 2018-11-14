class Rectangle(object):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def circumference(self):
        return (self.length * 2) + (self.width * 2)

    def __str__(self):
        return "Width: {} Height: {}".format(self.length, self.width)

    def __eq__(self, other):
        return self.area() == other.area()


def main():
    r = Rectangle(10, 20)
    print(r)
    print(r.area())
    print(r.circumference())
    r2 = Rectangle(10, 21)
    print(r2)
    if r == r2:
        print("The two rectangles are equally large")
    else:
        print("The two rectangles are not equal")


main()
