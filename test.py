print("hello world")
print("hello world again")

from pathlib import Path
import csv
import requests

api_key = "BRB9X55YUVV8G334"
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'


response = requests.get(url)
print(response)
data = response.json() 
print(data)

