class Superhero(object):
    def __init__(self, name="", age=0, superpower="n"):
        self.name = name
        self.age = age
        self.superpower = superpower

    def set_name(self, other):
        self.name = other

    def set_age(self, other):
        self.age = other

    def set_super_power(self, other):
        if other == "f":
            self.superpower = "Flying"
        elif other == "g":
            self.superpower = "Giant"
        elif other == "h":
            self.superpower = "Hacker"
        elif other == "n":
            self.superpower = "None"
        else:
            self.superpower = "Weakling"

    def __str__(self):
        return "{} ({}): {}".format(self.name, self.age, self.superpower)


adam = Superhero("Adam", 10)
adam.set_super_power("h")
print(adam)
