import re

pattern = re.compile(r"\d{3} \d{3}-? \d{4}")
result = pattern.search("Call me at 987 654 3210")
print(result.group())