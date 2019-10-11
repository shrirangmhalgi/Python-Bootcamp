nested_list = [list(range(11)), list(range(11, 21)), list(range(21, 31))]

print(nested_list)

# printing values in nested list
for l in nested_list : 
    for item in l :
        print(item)


# nested list comprehension
[[print(val) for val in l] for l in nested_list]
[[print(val) if val % 2 == 0 else print(val * 10) for val in l] for l in nested_list]