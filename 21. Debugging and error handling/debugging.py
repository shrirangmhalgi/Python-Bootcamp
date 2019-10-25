import pdb

first = "first"
second = "second"
pdb.set_trace()
result = first + second
third = "third"
result += third
print(result)

# common pdb commands
# l -> list
# n -> next line
# p -> print
# c -> continue / finishes debugging