import pandas
import json
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import requests

companyname2 = input("What is the name of the company you'd like stock prices for? ")
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


company = get_symbol(companyname2)

print("Cool, " + company + " it is!")
print("")

# Input the name of the company
companyname = companyname2

ts = TimeSeries(key='PIUH8SB6UWPJ7Q14', output_format='pandas')
data, meta_data = ts.get_intraday(symbol=companyname,interval='1min', outputsize='full')

pprint(data.head(1))
