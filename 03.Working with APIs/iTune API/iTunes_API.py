import requests
import json

base_site = "https://itunes.apple.com/search"

response = requests.get(base_site,params={"term":"fifth harmony", "country":"us","limit": 200})

print(response.url)
print(response.status_code)

info = response.json()
print(json.dumps(info, indent=4))

#name and release dates of the songs
for result in info['results']:
    print(result['trackName'])
    print(result['releaseDate'])
    
