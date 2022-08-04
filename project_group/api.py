from locale import currency
from pathlib import Path
import csv
import requests



def CURRENCY_EXCHANGE_RATE():
    """
    converts 1 USD to SGD 
    """
    api_key = "BRB9X55YUVV8G334"
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    for value in data:
        return float(data[value]['5. Exchange Rate'])



def get_conversion_rate():
    f = open("summary_report.txt", "a")
    f.write("[REAL TIME CURRENCY CONVERSION RATE] ")
    
    f.write(f"USD1 = SGD{CURRENCY_EXCHANGE_RATE()}\n")