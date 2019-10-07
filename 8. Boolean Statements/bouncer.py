age = int(input("Enter your current age...\n"))

if age >= 18 and age < 21:
    print("You need to wear a wristband...")
elif age >= 21:
    print("You get a normal entry...")
else:
    print("No entry inside the club...")
    