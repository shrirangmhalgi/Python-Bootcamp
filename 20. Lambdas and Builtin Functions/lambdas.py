def square(num):
    return num * num

print(square(2))

# lambda is a one line function
square2 = lambda num : num * num
print(square2(2))

# __name__ property returns name of the function
print(square.__name__)
print(square2.__name__)

# map(function, iteratable object)
list1 = list(range(0, 10))
maps = list(map(lambda x : 2 * x , list1))
print(maps)

# filter()
list1 = list(range(0, 10))
evens = list(filter(lambda x : x % 2 == 0, list1))
print(evens)

new_list = list(map(lambda x : x + 5, filter(lambda x : x % 2 == 0, list1)))
print(new_list)