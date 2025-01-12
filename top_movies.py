from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.netflix.com/tudum/top10/most-popular")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
titles = soup.find_all(name="td", class_="title")

movies_and_rank = []

for title in titles:
    movie_title = title.find("button").getText()
    move_rank = title.find(name="span", class_="rank").getText()
    movies_and_rank.append((move_rank, movie_title))


with open("top10movies.txt", mode="w") as file:
    for movie in movies_and_rank:
        file.write(f"{movie[0]} - {movie[1]}\n")
