# 1. get request
# 2. ask server for json using the headers property as {"Accept" : "application/json"}
# 3. convert it to python code using response.json

import requests

URL = "https://icanhazdadjoke.com/"

res = requests.get(URL, headers={"Accept" : "application/json"})
print(res.text)
print(res.json())
