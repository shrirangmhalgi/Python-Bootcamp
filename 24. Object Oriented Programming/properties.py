class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    # getter
    @property
    def age(self):
        return self._age
    
    # setter
    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age cannot be negative")
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


# be careful with _variable and variable and getters and setters
shrirang = Human("shrirang", "mhalgi", 21) 
print(shrirang.age)
shrirang.age = 20
print(shrirang.age)
print(shrirang.__dict__) # returns the key and value of the class attributes
shrirang.full_name = "Gauri Mhalgi" # if more spaces are given then valueerror
print(shrirang.__dict__)