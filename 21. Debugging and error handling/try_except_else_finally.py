try:
    num = int(input("Enter a number... : "))
except ValueError as err:
    print(err)
else:
    print(num)
finally:
    print("done")