def log_function_data(function):
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

# -----OUTPUT-----
# I am a wrapper function
# wrapper

# The issue with decorator is it calls the wrapper functions metadata
# The solution for the issue is in decorator_issue_solution.py 