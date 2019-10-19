# variable arguments gets passed as a tuple
def var_args(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(var_args(1, 3, 2, 4, 5, 5))