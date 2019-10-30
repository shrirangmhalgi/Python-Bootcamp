class Animal:
    def __init__(self, name, species):
        self.species = species
        self.name = name
    

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    def __init__(self, name, breed, favourite_toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.favourite_toy = favourite_toy

    def __repr__(self):
        return f"{self.name} is a {self.breed} {self.species} and likes to play with {self.favourite_toy}"

a = Cat("Blue", "Scottish", "Wool")
a.make_sound("Chirp")
print(isinstance(a, Animal)) # -> True
print(a)
print(a.name)
print(a.breed)