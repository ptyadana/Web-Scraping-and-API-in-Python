#Obtaining Historical Exchange Rates
import requests
import json

base_url = "https://api.exchangeratesapi.io"

historical_date_url = base_url + "/2020-04-12"

response = requests.get(historical_date_url)
data = response.json()

# data = {'rates': {'CAD': 1.5265, 'HKD': 8.4259, 'ISK': 155.9, 'PHP': 54.939, 'DKK': 7.4657, 'HUF': 354.76, 'CZK': 26.909, 'AUD': 1.7444, 'RON': 4.833, 'SEK': 10.9455, 'IDR': 17243.21, 'INR': 82.9275, 'BRL': 5.5956, 'RUB': 80.69, 'HRK': 7.6175, 'JPY': 118.33, 'THB': 35.665, 'CHF': 1.0558, 'SGD': 1.5479, 'PLN': 4.5586, 'BGN': 1.9558, 'TRY': 7.3233, 'CNY': 7.6709, 'NOK': 11.2143, 'NZD': 1.8128, 'ZAR': 19.6383, 'USD': 1.0867, 'MXN': 26.0321, 'ILS': 3.8919, 'GBP': 0.87565, 'KRW': 1322.49, 'MYR': 4.7136}, 'base': 'EUR', 'date': '2020-04-09'}

print(json.dumps(data, indent=4, sort_keys=True))

# Invalid URL
invalid_url = base_url + "/2019-12-01" + "?symbols=USB"
response = requests.get(invalid_url)

print(response.status_code)
print(response.json())
# 400 for bad request
#invalid response = {'error': "Symbols 'USB' are invalid for date 2019-12-01."}