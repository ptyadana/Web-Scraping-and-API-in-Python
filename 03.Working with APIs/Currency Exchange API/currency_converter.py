import requests
import json

base_url = "https://api.exchangeratesapi.io/"

print("***** Welcome to Currency Converter ****")
date = input("Please enter the date (in the format 'yyyy-mm-dd') OR type 'latest' : ")
base_currency = input("Currency converted from (example: 'USD') : ")
to_currency = input("Currency converted to (example: 'JPY') : ")
amount = input(f"How much {base_currency} do you want to convert? : ")

if date and base_currency and to_currency and amount:

    param_url = base_url + date + "?symbols=" + base_currency + "," + to_currency

    if date == 'latest':
        param_url = base_url + "latest?symbols=" +  base_currency + "," + to_currency
    
    response = requests.get(param_url)

    if response.ok is False:
        print(f"Opps! Seem like there is an Error {response.status_code}. Please try again.")
        print(f"{response.json()['error']}")
        
    else:
        data = response.json()

        #testing
        # base_currency = 'USD'
        # to_currency = 'JPY'
        # amount = 100
        # data = {'rates': {'JPY': 117.55, 'USD': 1.0936}, 'base': 'EUR', 'date': '2020-04-01'}
        
        converted_amount = (float(amount) / float(data['rates'][base_currency])) * float(data['rates'][to_currency])
        converted_amount = round(converted_amount,2)

        print(f"The amount equalivant to {base_currency} {amount} is {to_currency} {converted_amount}")

else:
    print("You have provided invalid information. Please try again.")
