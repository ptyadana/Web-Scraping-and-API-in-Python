import requests
import json

base_url = 'https://api.exchangeratesapi.io/latest'

#reqeust to API
response = requests.get(base_url)

#investigating response
print(response.ok)
print(response.status_code)
print(response.text)

#handling JSON
json_response = response.json()

#to void calling to API so many time, just for testing purpose
# json_response = {'rates': {'CAD': 1.5265, 'HKD': 8.4259, 'ISK': 155.9, 'PHP': 54.939, 'DKK': 7.4657, 'HUF': 354.76, 'CZK': 26.909, 'AUD': 1.7444, 'RON': 4.833, 'SEK': 10.9455, 'IDR': 17243.21, 'INR': 82.9275, 'BRL': 5.5956, 'RUB': 80.69, 'HRK': 7.6175, 'JPY': 118.33, 'THB': 35.665, 'CHF': 1.0558, 'SGD': 1.5479, 'PLN': 4.5586, 'BGN': 1.9558, 'TRY': 7.3233, 'CNY': 7.6709, 'NOK': 11.2143, 'NZD': 1.8128, 'ZAR': 19.6383, 'USD': 1.0867, 'MXN': 26.0321, 'ILS': 3.8919, 'GBP': 0.87565, 'KRW': 1322.49, 'MYR': 4.7136}, 'base': 'EUR', 'date': '2020-04-09'}

#Python Built in package json
#loads(string): converts a JSON formatted string to a Python Object
#dumps(obj): converts a Python Object to a regular string, with options to make the string prettier
print(json.dumps(json_response, indent=4))