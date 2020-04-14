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
    a_name = a.name

    #Getting attribute value (2 ways)
    href_value = a['href']
    href_value = a.get('href')

    #class values will be list as each html element can have multiple classes
    href_class_list = a['class']
    href_class_list = a.get('class')
    
    #difference between those 2 methods
    #using dictionary style will raise Key Error, if there is no key
    #get method will return NONE, if there is no such element
    print(a.get('blah'))
    print(repr(a.get('blah'))) #return as string

    #dictionary style attributes
    a_attributes = a.attrs
    print(a_attributes)

    