def name(first, second):
    print(f"{first} says hello to {second}")

names = {"first" : "shrirang", "second" : "mhalgi"}
name(**names)

# dictionary gets unpacked into keyword arguments