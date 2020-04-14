import requests
from bs4 import BeautifulSoup

#Making GET request
base_url = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_url)

if response.status_code:
    html = response.content

    #Making the soup
    soup = BeautifulSoup(html, "html.parser")

    #Extracting data from HTML tree
    a = soup.find('a', class_ = 'mw-jump-link')

    a_string = a.string
    a_string = a.text
    print(a_string)


    #text vs string
    p = soup.find_all('p')[1]
    # print(p.text)

    #.strings and .stripped_strings
    for s in p.strings:
        print(s)


    for s in p.stripped_strings:
        print(s)