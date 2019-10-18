print({i ** 2 if i % 2 == 0 else i for i in range(10, 100, 5)})

print({i ** 2 for i in range(10, 100, 5) if i % 2 == 0})