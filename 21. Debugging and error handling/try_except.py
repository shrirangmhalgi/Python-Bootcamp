try:
    foobar
except NameError as err:
    print("Problem")
print("Problem solved")

d = {"name" : "shrirang"}

def get_key(d, key):
    try:
        return d[key]
    except KeyError as k:
        return f"{key} does not exist in dictionary"

print(get_key(d, "name"))
print(get_key(d, "surname"))
