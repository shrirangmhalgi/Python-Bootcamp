def square(num = 0):
    return num * num

print(square())
print(square(2))
print(square(3))


# default parameters as function
def add(a, b):
    return a + b

def math(a, b, fn = add):
    return fn(a, b)

def subtract(a, b):
    return a - b

print(math(10, 20))
print(math(10, 1, subtract))