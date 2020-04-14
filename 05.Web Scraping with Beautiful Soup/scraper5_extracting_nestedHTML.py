import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

#Extracting data from nested tags
div_notes = soup.find_all('div', {'role':'note'})
div_links = [div.find('a') for div in div_notes]

articles = [link.string for link in div_links]
articles_links = [urljoin(base_url, link.get('href')) for link in div_links]

print(articles)
print(articles_links)

# shorter version
# articles = [article.find('a').string for article in div_notes]
# print(main_articles)