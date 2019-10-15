# dictionaries do not gurantee the order 
# keys can be numbers or strings
# values can be anything
sample_dictionary = {
    "first_name" : "shrirang",
    "middle_name" : "rajendra",
    "last_name" : "mhalgi"
}

print(sample_dictionary)

sample_dictionary2 = dict(first_name = "gauri", middle_name = "rajendra", last_name = "mhalgi")

print(sample_dictionary2)

# accessing a single value
print(sample_dictionary["first_name"])

# accessing dictionary keys
for k in sample_dictionary.keys() :
    print(k)

for k in sample_dictionary :
    print(k)

# accessing dictionary values
for v in sample_dictionary.values() :
    print(v)
    
# accessing tuples
for k in sample_dictionary.items() :
    print(k)  

# accessing keys as well as values 
for k, v in sample_dictionary.items() :
    print(k, v)

# accessing whether a key exists in dictionary
print("first_name" in sample_dictionary)

# accessing whether a value exists in dictionary
print("shrirang" in sample_dictionary.values())

# some dictionary methods
# 1. clear
print(sample_dictionary2.clear()) # -> returns None

# 2. copy -> creates a copy of the dictionary
d = sample_dictionary2.copy()
print(d)

# 3. setting the default values to the dictionary
print({}.fromkeys(["a", "b", "c", "d"], "unknown"))
print({}.fromkeys("shrirang", "unknown"))

# 4. get returns the value if exists else returns none
print(sample_dictionary.get("first_name"))

# 5. pop removes item from the dictionary
print(sample_dictionary.pop("first_name"))

# 6. popitem removes a random item from the dictionary
print(sample_dictionary.popitem())

# 7. update is used to update a dictionary item
sample_dictionary.update(dict(name = "shri"))
print(sample_dictionary)