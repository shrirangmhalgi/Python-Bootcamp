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

"""
retrieves item with index 5
alist[5]

retrieves item's between index 1 & index 10 (but not index 10)
alist[1:10]

retrieves every 2nd item between index 1 & index 10 (but not index 10)
alist[1:10:2]

returns the list item in the array
alist[-1]

returns the 3rd last item in the array
alist[-3]

1. Reversing a list: alist[::-1]
2. Removing every nth element of the list alist[n-1::n]
3. Pop off the last n elements alist[:-n]
4. Shift the first n elements alist[n:]
5. Get a list of numbers with index divisble by nlist(range(500))[::n]
"""