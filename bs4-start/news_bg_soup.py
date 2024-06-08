from bs4 import BeautifulSoup
import html
import requests

respond = requests.get("https://news.bg")
web_text = respond.text
soup = BeautifulSoup(web_text, "html.parser")
main_artical = soup.find(class_="news-info")
print(main_artical.select_one(selector='h2').text)


link = soup.find(class_="main-thumb").get("href")
print(link)