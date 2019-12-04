# with statement calls the __enter__() at start and __exit__() at the end
with open("story.txt") as file:
    data = file.read()

print(data)
print(file.closed)