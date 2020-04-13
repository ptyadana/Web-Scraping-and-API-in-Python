import requests
import json

base_url = "https://jobs.github.com/positions.json"

#Extracting results from multiple pages
results = []

for index in range(10):
    response = requests.get(base_url, params= {"description":"python", "location":"new york","page": index+1})
    
    print(response.url)
    # print(response.json())
    if len(response.json()) == 0:
        break

    results.extend(response.json())

print(len(results))








data = response.json()
data = json.dumps(data, indent=4)

