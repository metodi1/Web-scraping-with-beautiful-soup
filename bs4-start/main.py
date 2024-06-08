from bs4 import BeautifulSoup
import html
import requests

respond = requests.get("https://news.ycombinator.com/")

web_yc_web_page = respond.text
soup = BeautifulSoup(web_yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_titles = []
article_links = []
article_scores = []

for article in articles:
    article_titles.append(article.getText())
    article_links.append(article.find("a")["href"])

sub_lines = soup.find_all(class_="subtext")
for sub_line in sub_lines:
    text_score = sub_line.getText()
    split_score = text_score.split(" ")
    score = int(split_score[0])
    article_scores.append(score)
    max_score =max(article_scores)
    index_max = article_scores.index(max_score)

print(article_titles[index_max])
print(article_links[index_max])
print(max_score)

# with open("website.html",encoding='utf-8') as file: 
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# #print(soup.title)
# #print(soup.title.string)
# #print(soup.prettify())
# #print(soup.ul)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.text)
#
# find_class = soup.find(name="h3", class_="heading")
# print(find_class)
#
# company_url=soup.select_one(selector="p a")
# print(company_url)
