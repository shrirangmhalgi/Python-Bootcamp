# len() function can be used to find length of anything..

# lists start with [ and end with ] and are csv

task = ["task 1", "task 2",  "task 3"]
print(len(task)) # prints the length of the list...

list1 = list(range(1, 10)) # another way to define a list

# accessing data in the lists 
# lists are accessed like arrays.. 0, 1, 2 ... and to count it backwards, start with negative -1, -2, -3 ...
print(task[0])
print(task[1])
print(task[2])
 
# to check if value exists in a list or not use the in operator
print("task 1" in task)

# iterate through lists
for i in task :
    print(i)

i = 0
while i != len(task) :
    print(f"task {i} : " + str (task[i]))
    i += 1

# some list methods
# 1. append(123) -> appends the data in the list
a = []
a.append(1)
print(a)

# 2. extend([list]) -> attaches multiple items to the list
a.extend([2, 3, 4])
print(a)

# 3. insert(position, data)
a.insert(2, "shrirang")
print(a)

# 4. clear() removes all the elements from the list
a.clear()
print(a)

# 5. pop(index number)
a.extend([2, 3, 4])
a.pop() # -> removes last element from the list
a.pop(0) # -> removes the element specified by index number
print(a)

# 6. remove(x) x is a value but remove does not return a value
a.remove(3)
print(a)

# 7. index(value) returns the first index of the value present in the list
a.extend([2, 3, 4])
print(a.index(2))
print(a.index(2, 1)) # -> finds the first index of 2 starting from 1
print(a.index(2, 1, 2)) # -> finds the first index of 2 starting from 1 and ending index of 2

# 8. count() -> returns the count of the number present in the list
print(a.count(2))

# 9. reverse() -> reverses the current list
a.reverse()
print(a)

# 10. sort()
a.sort()
print(a)

# 11. join
" ".join(a)










# tasks = ["task " + str(i) for i in range(1, 4)]
# print(tasks)

# a=[0]*10
# b=[0 for i in range(10)]

# print(a)
# print(b)

# a[2]=9
# b[2]=9

# print(a)
# print(b)
