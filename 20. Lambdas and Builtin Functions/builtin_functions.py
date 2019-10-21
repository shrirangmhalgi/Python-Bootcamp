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

# 9. abs returns the absolute value of a number
print(abs(-1.2))
print(abs(-1))
print(abs(1.2))
print(abs(1))
 
# 10. sum returns the sum of the collection
print(sum(list1, 100))

# 11. round rounds off the given number
print(round(1.212121, 2))
print(round(1.5))

# 12. zip is used to bind 2 or more collections together it stops as soon as the shortest iterable is exhausted
list1 = list(range(10, 20))
list2 = list(range(20, 30))
print(dict(zip(list1, list2)))

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']
print({pair[0] : max(pair[1], pair[2]) for pair in zip(students, midterms, finals)})

print(dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals)))))
print(dict(zip(students, map(lambda pair: ((pair[0] + pair[1]) / 2), zip(midterms, finals)))))