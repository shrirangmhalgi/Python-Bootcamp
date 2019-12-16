import re

text = "Last week Mr. Shri and Ms. Shri killed Mr. Omi"
pattern = re.compile(r"(Mr\.|Ms\.|Mrs\.) ([a-z])[a-z]+", re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)