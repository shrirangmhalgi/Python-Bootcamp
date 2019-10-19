# the values are passed to the function as dictionary
def name(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}'s a {v}")

name(shrirang = "name", mhalgi = "surname")

# parameter ordering in python is as follows
# 1. parameter
# 2. *args
# 3. default parameters
# 4. **kwargs