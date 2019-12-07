import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"
    
    def make_sound(self, sound):
        print(f"This animal makes {sound}")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

# blue = Cat("Blue", "Scottish Fold", "String")

# with open("pickling.pickle", "wb") as file:
#     pickle.dump(blue, file)

with open("pickling.pickle", "rb") as file:
    ghostly_blue = pickle.load(file)
    print(ghostly_blue)