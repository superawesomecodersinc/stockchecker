# Import statements
## Some are marked as not used, they are, computers know nothing.
import pandas
import json
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import requests
import sys
import matplotlib.pyplot as plt

# Input Statement #1
companyname2 = input(
    "What is the name of the company you'd like stock prices for? ")

# Capitalises the symbol you put in above
companynameupper = companyname2.upper()

# The below code is a definition for the Yahoo Finance API which returns the company name from the symbol input
def get_symbol(symbol):
	url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(
	    symbol)

	result = requests.get(url).json()

	for x in result['ResultSet']['Result']:
		if x['symbol'] == symbol:
			return x['name']


# Changes the name of the string for the stock price API call below
company = get_symbol(companynameupper)

# Prints the company name collected from Yahoo Finance
print(company + " it is!")
print("")
print("We're just retrieving your data...")
print("")

# Changes the company string for the call below
companyname = companynameupper

ts = TimeSeries(key='PIUH8SB6UWPJ7Q14', output_format='pandas')
data, meta_data = ts.get_intraday(
    symbol=companyname, interval='1min', outputsize='full')

# Pretty Prints the data returned above
pprint(data.head(1))
# Queries about the stock buying bit
print ("")
print ("Do you want a graph?")

# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = input().lower()
if choice in yes:
	print ("One graph, coming right up!")
	print ("")
	data, meta_data = ts.get_intraday(symbol=companyname,interval='1min', outputsize='full')
	data['4. close'].plot()
	plt.title('Intraday Times Series for the ' + company + ' stock (1 min)')
	plt.show()
elif choice in no:
	print("")
	print ("Thank you and goodnight!")
	print("")
else:
   sys.stdout.write("Please try again, and respond with 'yes' or 'no'")
