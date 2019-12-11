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
# data = soup.body.contents -> returns all the contents of the tag.
# data = soup.body.contents[1].contents[1].next_sibling.next_sibling.previous_sibling -> returns the next sibling of the data
# data = soup.body.contents[1].contents[1].parent.parent -> returns the parent of the current element
# data = soup.find(class_="hero-quote").find_next_sibling()
data = soup.find(class_="hero-quote").find_next_sibling(class_="hero-image")
data = soup.find(class_="hero-quote").find_previous_sibling()
data = soup.find(class_="hero-quote").find_parent()
data = soup.find(class_="hero-quote").find_parent("html")
print(data)
