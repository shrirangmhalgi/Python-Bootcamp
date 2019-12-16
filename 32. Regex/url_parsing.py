import re

# https?://www\.[a-zA-Z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*
url_regex = re.compile(r"(https?)://(www\.[a-zA-Z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
result = url_regex.search("https://www.google.com")
print(result.group())
print(result.groups())