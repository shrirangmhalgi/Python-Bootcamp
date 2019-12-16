import re

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "Days of Anna (2014)",
    "Babycakes (1984)" 
]

pattern = re.compile(r"(^[\w ]+) \((\d{4})\)$")
new_list = []
for title in titles:
    result = pattern.sub("\g<2> - \g<1>", title)
    new_list.append(result)
    
new_list.sort()
print(new_list)