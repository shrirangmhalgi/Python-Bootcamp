some_list = list(range(0, 21))
print(some_list)

print(some_list[2:])  # end is implicit
# slicing starts from 1
# slicing can also done in a negative manner in this it moves that many rows back and goes till the end

# start : end : step (if you dont give start end or slice it assumes the default value) 
print(some_list[:4]) # the end parameter is exclusive and the start is implicit if not given
print(some_list[:-1]) # start to second last
print(some_list[::2]) # taking every alternate number i.e. using the step count

# if you add negative step count then you get the revered version of the list
print(some_list[1::-1])
print(some_list[:1:-1])
print(some_list[::-1])

# some extra cool tricks with slicing
# 1. reversing a string
string = "this is fun...!"
print(string[::-1])

# 2. modifying specific portion of the list
some_list[2:15] = ["a", "b", "c"]
print(some_list)
print(str(some_list[6])[::-1])

# swapping the values in python
my_name = ["shrirang", "rajendra", "mhalgi"]
my_name[0], my_name[2] = my_name[2], my_name[0]
print(my_name)