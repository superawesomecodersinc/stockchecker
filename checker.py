import pandas
import json
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

# Input the name of the company
companyname = input("Give the symbol of the company you would like to see the stock stats of (e.g. GOOGL for Alphabet Inc.")
ts = TimeSeries(key='PIUH8SB6UWPJ7Q14', output_format='pandas')
data, meta_data = ts.get_intraday(symbol=companyname,interval='1min', outputsize='full')
pprint(data.head(1))
