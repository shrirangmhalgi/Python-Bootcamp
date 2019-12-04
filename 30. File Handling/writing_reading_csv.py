# from csv import reader, writer
# with open("file.csv") as file:
#     csv_reader = reader(file)
#     with open("file1.csv", mode="w") as file:
#         csv_writer = writer(file)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])

from csv import DictReader, DictWriter
with open("file.csv") as file:
    csv_reader = DictReader(file)
    with open("file2.csv", mode="w") as file:
        csv_writer = DictWriter(file, fieldnames=["Name", "Address", "Age"])
        csv_writer.writeheader()
        csv_writer.writerow({
            "Name" : "Shrirang",
            "Address" : "Pune",
            "Age" : 21 
        })