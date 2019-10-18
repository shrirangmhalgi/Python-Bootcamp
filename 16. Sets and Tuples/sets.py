# sets do not have duplicate values
# elements in sets are not ordered
# set does not throw error for dupulicates but it returns a single value

s = {1, 2, 3}
s1 = set({1, 2, 3})

print(3 in s)

# accessing numbers in set
for n in s: 
    print(n)

# convert list to set and back to list if you want to eliminate dupliacates
# set methods
# 1. add -> adds element to the set
s.add(4)

# 2, remove -> removes element from the set
s.remove(1)

# 3. discard removes the element and if not there does nothing
s.discard(2) 
print(s)

# 4. copy creates a shallow copy of the set
t = s.copy()

# 5. clear
t.clear()
print(t)

s = {i for i in range(0, 10)}
s1 = {i for i in range(5, 15)}
print(s | s1) # | is for union
print(s & s1) # & is for intersection