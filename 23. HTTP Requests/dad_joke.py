# 1. get request
# 2. ask server for json using the headers property as {"Accept" : "application/json"}
# 3. convert it to python code using response.json

from requests import get
from pyfiglet import figlet_format
from random import choice

URL = "https://icanhazdadjoke.com/search"

print(figlet_format("Dad joke 3000"))

term = input("Enter the topic you want to search...! : ")
result_list = get(
    URL,
    headers={
        "Accept": "application/json"},
    params={
        "term": term}).json()['results']

# limit = input("Enter the number of jokes you want to search...! : ")
# res = requests.get(URL, headers={"Accept" : "application/json"}, params={"term" : term, "limit" : limit})

flag = False
if len(result_list) == 0:
    print(f"I have got no joke on {term}... Please try again")
elif len(result_list) == 1:
    print(f"I have got one joke on {term}... Here it is")
    flag = True
else:
    print(f"I have got {len(result_list)} jokes on {term.upper()}... Heres one")
    flag = True

if flag:
    print(choice(result_list)['joke'])


# for i in range(0, len(result_list)):
#     print(f"{i + 1}. {result_list[i]['joke']} \n")
