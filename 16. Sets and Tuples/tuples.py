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

#looping through tuples
for num in numbers:
    print(num)

i = len(numbers) - 1
while i >= 0 :
    print(numbers[i])
    i -= 1

# tuple methods
# 1. count returns the number of times the item is present in the tuple
print(numbers.count(1))

# 2. index returns the first index of the value in the tuple
print(numbers.index(1))