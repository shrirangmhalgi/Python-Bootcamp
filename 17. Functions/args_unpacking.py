def sum(*args):
    total = 0
    for i in args:
        total += i
    print(total)

sum(*[1, 2, 3, 4, 5])
sum(*(1, 2, 3, 4, 5))

'''works for both list and tuple '''
