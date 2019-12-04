# you need to add some backslash characters if you want a newline
# with open("abc.txt", mode="w") as file:
#     file.write("Hey bud how are you..?\n")
#     file.write("Hey bud how are you..?")

# with open("abc.txt", mode="a") as file:
#     file.write("Hey bud how are you..?\n")
#     file.write("Hey bud how are you..?\n")

with open("abc.txt", mode="r+") as file:
    file.write("Hey bud how are you..?\n")
    file.write("Hey bud how are you..?\n")