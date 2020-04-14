import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#Making GET request
base_url = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_url)

if response.status_code:
    html = response.content

    #Making the soup
    soup = BeautifulSoup(html, "html.parser")

    links = soup.find_all('a')
    
    link = links[26]
    link_value = link.string
    link_href = link.get('href')

    #Making full url
    link_full_url = urljoin(base_url, link_href)
    print(link_full_url)

    #Processing multiple links at once
    for item in links:
        item_value = item.string
        item_url = urljoin(base_url, item.get('href'))
        # print(item_value, item_url)

    #using list comprehension
    clean_links = [link.get('href') for link in links if link.get('href') is not None]
    
    full_urls = [urljoin(base_url, clean_url) for clean_url in clean_links]
    print(full_urls)

    #getting internal links
    internal_links = [url for url in full_urls if 'wikipedia.org' in url]
    print(internal_links)