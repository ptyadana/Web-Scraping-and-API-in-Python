import requests
import json

base_url = 'https://api.exchangeratesapi.io/latest'

param_url = base_url + '?symbols=USD,GBP'

response = requests.get(param_url)
data = response.json()

# data = {'rates': {'USD': 1.0867, 'GBP': 0.87565}, 'base': 'EUR', 'date': '2020-04-09'}

print(type(data))
print(data)

rates = data['rates']['USD']
print(rates)
