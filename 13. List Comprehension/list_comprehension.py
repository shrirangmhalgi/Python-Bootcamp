some_list = list(range(1, 10))
print(some_list)

# list comprehension is basically using for loop to change each value in the list and return a new list
print([a * 10 for a in some_list])
print([a * 10 for a in range(1, 21, 2)])

# list comprehension with conditional operators
# 1. if
print([a for a in some_list if a % 2 == 0])
print([a for a in some_list if a % 2 != 0])

# 2. if else
print([a * 10 if a % 2 == 0 else a * 5 for a in some_list])

# 3. join
with_vowels = "This is shrirang"
print("".join([char for char in with_vowels if char not in "aeiou"]))


