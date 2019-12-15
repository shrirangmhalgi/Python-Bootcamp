import re

def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)

def is_valid_phone(input):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

    
print(extract_phone("My phone number is 987 654-3210"))
