name = "shrirang"

def my_name():
    global name 
    name += " mhalgi"
    return f"your name is {name}"

print(my_name())

# you cant change the name value however you can declare a same variable which has local scope

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()

print(outer())