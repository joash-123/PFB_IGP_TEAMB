print("hello world")
print("hello world again")

from locale import currency
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

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(data)


fp = Path.cwd()/"currency.csv"
fp.touch()
with fp.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer =  csv.writer(file)
    # write header
    writer.writerow(["Forex weekly prices", "From USD", "To SGD", "Last Refreshed", "Time Zone (UTC)"])
    # iterate over data to write data in csv file
    for data in currency["data"]:
        writer.writerow([data["date"], data["value"],data["value"],data["value"],data["value"]])


print("hello")        