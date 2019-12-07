import jsonpickle

class Cat:
    def __init__(self, name, breed, toy):
        self.name = name
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

c = Cat("Blue", "Scottish Fold", "String")

# with open("cat.json", "w") as file:
#     json_c = jsonpickle.encode(c)
#     file.write(json_c)

with open("cat.json", "r") as file:
    contents = file.read()
    json_c = jsonpickle.decode(contents)
    print(json_c)