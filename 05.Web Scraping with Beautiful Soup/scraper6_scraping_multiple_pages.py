import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

div_notes = soup.find_all('div', {'role':'note'})
div_links = [div.find('a') for div in div_notes]

articles_links = [urljoin(base_url, link.get('href')) for link in div_links]

#Scraping multiple pages automatically
par_text = []
i = 0

for url in articles_links:
    article_response = requests.get(url)

    if article_response.status_code == 200:
        print(f'URL {i+1}, {url}')
    else:
        print(f'status code {article_response.status_code} : skipping URL {i+1}, {url}')
        i = i+1
        continue

    article_html = article_response.content
    article_soup = BeautifulSoup(article_html, 'lxml')
    article_pars = article_soup.find_all('p')

    text = [p.text for p in article_pars]
    par_text.append(text)
    i = i+1


page_text = ["".join(p_text) for p_text in par_text]
# print(page_text[0])

#zipping as dictionary
dict_articles_pages = dict(zip(articles_links, page_text))
print(dict_articles_pages['https://en.wikipedia.org/wiki/Music_education'])