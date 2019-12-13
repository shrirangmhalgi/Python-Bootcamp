# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["date", "title", "content", "url"])
    
    i = 0
    while i != 10:
        i += 1
        response = requests.get("https://www.rithmschool.com/blog?page="+ str(i))
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            a_tag = article.find("a")
            title = a_tag.get_text()
            url = a_tag["href"]
            date = article.find("time")["datetime"]
            content = article.find("p").get_text()
            try:
                csv_writer.writerow([date, title, content, url])
            except:
                pass