# assert statement is used to test something
# if a python file is run with -O flag, it ignores all the assertions

def add(x, y):
    assert x > 0 and y > 0, "Both the numbers should be positive"
    return x + y

print(add(1, 10))
print(add(-1, 10))
