from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article in articles:
    a = article.find("a")
    text = a.getText()
    link = a.get("href")
    article_texts.append(text)
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)
