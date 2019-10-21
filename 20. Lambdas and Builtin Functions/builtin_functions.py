import sys

# 1. all() returns true if ALL elements of iteratable are truthy
print(all(list(range(10))))
print(all(list(range(1, 10))))

# 2. any() returns true if ANY of the element is truthy
print(any(list(range(10))))
print(any(list(range(1, 10))))

# 3. sys.getsizeof
print(sys.getsizeof([x % 2 == 0 for x in range(1000)]))
print(sys.getsizeof((x % 2 == 0 for x in range(1000)))) # (x % 2 == 0 for x in range(1000)) is a generator

# 4. sorted() sorts things
list1 = list(range(10, 0, -1))
dict1 = [dict(name = "shrri"), dict(name = "hrri", last = "rang")]
print(sorted(list1))
print(sorted(list1, reverse = True))
print(sorted(dict1, key = lambda user : user['name'], reverse = True))

# 5. min() finds the minimum element 
print(min(list1))
print(min(list1, key = lambda n : n > 5))

# 6. max() finds the maximum element
print(max(list1))
print(max(list1, key = lambda n : n < 2))

# 7. reversed returns a reverse iterator
for i in reversed(list1):
    print(i)

print(''.join(list(reversed("hello world"))))

# 8. len
print("hello".__len__())