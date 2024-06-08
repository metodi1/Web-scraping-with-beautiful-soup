import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
moves_list = []

respond = requests.get(URL)
web_text = respond.text
soup = BeautifulSoup(web_text, "html.parser")
titles = soup.find_all(name="h3")

for title in titles:
    moves_list.insert(0,title.text)


#Write list to a text file
with open('movies.txt', 'w' , encoding='utf-8') as file:
     for item in moves_list:
         file.write(f"{item}\n")

for item in moves_list:
    print(item)