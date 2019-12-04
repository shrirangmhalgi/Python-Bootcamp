file = open("story.txt")
print(file.read())
# After a file is read, the cursor is at the end...
print(file.read())

# seek is used to manipulate the position of the cursor
file.seek(0) # Move the cursor at the specific position
print(file.readline()) # reads the first line of the file

file.seek(0)
print(file.readlines()) # Reads all the contents of the file and stores it in a list

# Make sure you close the files when you are done...
file.close()

# returns a value to check whether the file is closed or not...
file.closed