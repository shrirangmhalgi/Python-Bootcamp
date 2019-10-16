# tuples are immutable that is they cannot be changed
numbers = (0, 1, 2, 3, 4, 5)
print(numbers)
print(3 in numbers)

# tuples are faster than lists
# code is safe as it is immutable
# tuple is accessed using square brackets

# using tuples as keys in the dictionaries
locations = {
    (1.0, 2.0) : "London",
    (3.0, 2.0) : "India"
}

print(locations[(3.0, 2.0)])