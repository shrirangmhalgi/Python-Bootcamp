def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("0. exit")

    choice = int(input())
    if choice is 1:
        print(add(a, b))
    elif choice is 2:
        print(sub(a, b))
    elif choice is 3:
        print(mul(a, b))
    elif choice is 4:
        print(div(a, b))
    elif choice is 0:
        quit()
    else:
        print("Invalid choice")

