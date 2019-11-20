from functools import wraps # NOTE THIS IMPORT

def log_function_data(function):
    @wraps(function)  # NOTE THIS LINE
    def wrapper(*args, **kwargs):
        """I am a wrapper function"""
        print(f"You are about to call... {function.__doc__}")
        print(f"You are about to call... {function.__name__}")
        function(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """I am a add function"""
    return x + y

print(add.__doc__)
print(add.__name__)
help(wraps)

# -----OUTPUT-----
# I am a add function
# add
# @wraps() preserves the metadata of the function
