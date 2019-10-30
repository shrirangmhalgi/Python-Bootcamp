class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self, key):
        return f"The {key} you want is missing here..."

    def __setitem__(self, key, value):
        print("You want to change the dictionary..! \nWell Fine")
        super().__setitem__(key, value)


d = GrumpyDict({"first" : "Tom", "last" : "Jerry"})
print(d)