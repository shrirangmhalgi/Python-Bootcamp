import re

# def parse_name(input):
#     name_regex = re.compile(r"^(?P<title>Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)$")  # ?P<first> -> is a label for the group
#     matches = name_regex.search(input)
#     return matches.group("first")

# print(parse_name("Mr. Shrirang Mhalgi"))


# name_regex = re.compile(r"""
#     ^(?P<title>Mr\.|Mrs\.|Ms\.|Mdme\.)   # Name starts with Mr. or Ms. or Mrs. or Mdme.
#     \s                                   # Followed by a space
#     (?P<first>[a-zA-Z]+)                 # Followed by a first name
#     \s                                   # Followed by a space
#     (?P<last>[a-zA-Z]+)$                 # Followed by a last name
# """, re.VERBOSE | re.IGNORECASE)

name_regex = re.compile(r"""
    ^(?P<title>Mr\.|Mrs\.|Ms\.|Mdme\.)   # Name starts with Mr. or Ms. or Mrs. or Mdme.
    \s                                   # Followed by a space
    (?P<first>[a-zA-Z]+)                 # Followed by a first name
    \s                                   # Followed by a space
    (?P<last>[a-zA-Z]+)$                 # Followed by a last name
""", re.X | re.I)
match = name_regex.search("Mr. Omkar Gosavi")
print(match.group())
print(match.groups())

