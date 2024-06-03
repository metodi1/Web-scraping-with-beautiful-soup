from bs4 import BeautifulSoup
import html

with open("website.html",encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#print(soup.title)
#print(soup.title.string)
#print(soup.prettify())
print(soup.ul)