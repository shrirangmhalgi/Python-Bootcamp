from functools import wraps

def ensure_first_arg(value):
    def inner_function(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                return f"First arg needs to be {value}"
            return fn(*args, **kwargs)
        return wrapper
    return inner_function

@ensure_first_arg("Shrirang")
def name(*args):
    return args

print(name("Shrirang", "Coding", "Stocks"))
print(name("Sumi", "Coding", "Stocks"))

@ensure_first_arg(10)
def add_to_ten(*args):
    return args[0] + args[1]

print(add_to_ten(10, 20))
print(add_to_ten(1, 20))
