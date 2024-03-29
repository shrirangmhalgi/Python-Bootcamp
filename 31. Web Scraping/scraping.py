from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link href="https://fonts.googleapis.com/css?family=Source+Code+Pro:600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/image1.css">
  <title>Quote 1</title>
</head>
<body>
  <section class="hero-image">
    <div class="hero-quote">
      <p class="text">Someone's loss is someone's gain.</p>
    </div>
    <div class="hero-quote">
      <p class="text" id="shri">Fall forward.</p>
    </div>
  </section>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.div.p)
# print(soup.find("div"))
# print(soup.find_all("div"))
# print(soup.find(id='text'))
# print(soup.find(class_="text"))
# print(soup.find(attrs={"class" : "hero-image"}))
# print(soup.select(".hero-image")) -> css class
# print(soup.select("#hero-image")) -> css id
# print(soup.select("[hero-image]")) -> css attribute
print(soup.find("p")["class"])
# for i in soup.select(".text"):
#   print(i.get_text())
#   print(i.name)
#   print(i.attrs)