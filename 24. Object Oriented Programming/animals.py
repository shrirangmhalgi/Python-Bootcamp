class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land"

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name = name)

penguin = Penguin("Penguin")
print(penguin.walk())
print(penguin.greet())
print(penguin.swim())

# MRO or Method Resolution Order
# There is a complex algorithm behind MRO
# It is used to give method a priority
# you can see classes MRO by using the following 3 ways
# 1. mro()
# 2. help(class name)
# 3. __mro__