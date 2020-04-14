import requests
from bs4 import BeautifulSoup

#Making GET request
base_url = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_url)

if response.status_code:
    html = response.content
    print(html[:100])

    #Making the soup
    soup = BeautifulSoup(html, "html.parser")

    #Exporting HTML to file
    with open("wiki_music.html","wb") as file:
        file.write(soup.prettify('utf-8'))

    #Finding elements
    #find() , find_all()
    links = soup.find_all('a')
    print(isinstance(links,list))
    print(len(links))

    table = soup.find('tbody')
    table_type = type(table)

    td_tags = table.find_all('td')

    #Navigating the tree / children elements
    content = table.contents
    content_len = len(content)

    #Navigating up the tree
    parent = table.parent
    grandparent = table.parent.parent

    #Searching by Attributes
    div_tags = soup.find('div', id='siteSub')
    a_tags = soup.find_all('a', class_ ='mw-jump-link', href = '#p-search')
    
    #Searching method 2 | Placing attributes in Dictionary
    a_tags = soup.find('a', attrs = {'class':'mw-jump-link', 'href':'#p-search'})
    footer = soup.find('div', attrs={'id':'footer'})

    

   