# defining a function and a wrapper function and returning a wrapper function
def be_polite(fn):
    def wrapper_function():
        print("I am in wrapper function")
        fn()
        print("Exitting wrapper function")
    return wrapper_function

# @ sign defines a decorator
# it is same as:
# greet = be_polite(greet)
# greet()
@be_polite
def greet():
    print("My name is Shrirang")

greet()