from time import time
from functools import wraps

def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"Executing {function.__name__}")
        print(f"Time Elapsed : {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_gen():
    return sum(x for x in range(100000000))

@speed_test
def sum_list():
    return sum([x for x in range(100000000)])

print(sum_list())
print(sum_gen())