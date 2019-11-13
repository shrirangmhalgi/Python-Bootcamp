# iterator is object which can be iterated upon An object which returns data, one at a time when next() is called on it

name = "Shrirang"
iterator = iter(name)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # StopIteration error is thrown at the end of iterator

# iterable is object which returns a iterator when iter() method is called on it