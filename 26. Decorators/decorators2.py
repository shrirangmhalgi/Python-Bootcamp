# this does not work for multiple arguments so the solution is *args and **kwargs
# def shout(function):
#     def wrapper(name):
#         return function(name).upper()  
#     return wrapper

def shout(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()  
    return wrapper

@shout
def greet(name):
    return f"My name is {name}"

@shout
def order(item1, item2):
    return f"I would like to order {item1} and {item2} asap"

@shout
def lol():
    return f"lol"


print(greet("Shrirang"))
print(order("burger", "fries"))
print(lol())