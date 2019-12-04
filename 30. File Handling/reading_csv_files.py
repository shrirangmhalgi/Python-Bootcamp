# Normal file handling to read a file but it returns a giant string of data
# with open("file.csv") as file:
#     file.read()

# from csv import reader
# with open("file.csv") as file:
    # reader_csv = reader(file, delimiter="|")
#     next(reader_csv)
#     for fighter in reader_csv:
#         # each row is a list
#         # Header is included here so we can iterate on reader_csv object
#         print(f"{fighter[0]} is from {fighter[1]}")

from csv import DictReader
with open("file.csv") as file:
    reader_csv = DictReader(file, delimiter=",")
    for fighter in reader_csv:
        print(fighter["Name"])