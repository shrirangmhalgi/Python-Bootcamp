name = input("Enter a name:\n")
if name == "shrirang":
    print("Hello Shrirang")
elif name == "suvarna":
    print("Hello Suvarna")
elif name == "rajendra":
    print("Hello Rajendra")
else:
    print("Hello User")

# truthiness and falsiness
# (is) is used to evaluate truthiness and falsiness
# falsiness includes 
# None, Empty strings, Empty objecs and zero

# and or not
a = 1
b = 0
if a and b:
    print(f"{a} and {b} is true")
else:
    print(f"{a} and {b} is false")

if a or b:
    print(f"{a} or {b} is true")
else:
    print(f"{a} or {b} is false")

if not b:
    print(f"not {a} is {not a}")
