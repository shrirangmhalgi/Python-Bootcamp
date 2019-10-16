# normal comprehension
d = {"first" : 1, "second" : 2, "third" : 3}
print({key : value ** 2 for key, value in d.items()})

print({num : num ** 2 for num in range(0, 11)})

str1 = "abc"
str2 = "123"
combo = {str1[i].upper() : str2[i].upper() for i in range(0, len(str1))}
print(combo)

# conditional comprehension
print({f"number {num}" : (num ** 2 if num % 2 == 0 else num / 2) for num in range(0, 11)})

print({(k.upper() if k == 'first' else k) : v for k, v in d.items()})