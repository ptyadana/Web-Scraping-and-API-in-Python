import requests
import json
import pandas as pd

api_endpoint = "https://api.edamam.com/api/nutrition-details"

app_id = "d5df2415"
app_key = "b87fbe096f386ba8d6b2ad10dcc672d5"
url = api_endpoint + "?app_id=" + app_id + "&app_key=" + app_key

#Preparing POST request
headers = {
    "Content-Type": "application/json"
}

recipe = {
    "title" : "roasted chicken",
    "ingr" : ["1 (5 to 6 pound) roasting chicken", "Kosher salt", "Freshly ground black pepper"]
}

#Sending POST request
response = requests.post(url, headers=headers, json=recipe)
print(response.status_code)

info = response.json()
print(info.keys())

# data frame using pandas
nutrients = pd.DataFrame(info['totalNutrients']).transpose()
print(nutrients)

# export to csv
nutrients.to_csv("RoastedChicken_nutrients.csv")