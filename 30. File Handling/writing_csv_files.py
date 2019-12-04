from csv import writer
with open("file.csv", mode="w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Address", "Phone"])
    csv_writer.writerow(["Shrirang", "Pune", 9876543210])
    csv_writer.writerow(["Honey", "Bhusawal", 1234567890])
    csv_writer.writerow(["Pranav", "Jalgaon", 9876543210])
    csv_writer.writerow(["Ria", "Pune", 1234567890])