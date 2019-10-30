from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age
    
    def __add__(self, value):
        if isinstance(value, Human):
            return Human(value.first, self.last, 0)
        return TypeError("Only humans can be added")

    def __mul__(self, value):
        if isinstance(value, int):
            return [copy(self) for i in range(0, value)] # copy is used as it returns the same memory location
        return TypeError("Only integer expected to multiply")
    
a = Human("a", "b", 50)
b = Human("c", "d", 48)
c = a + b
print(c * 2)