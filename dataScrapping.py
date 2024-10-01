# Importing Libraries
import os
from dotenv import load_dotenv
load_dotenv()

from fredapi import Fred

fred_api_key = os.getenv('API_KEY')

# Creating the Fred Object
fred = Fred(fred_api_key)

cpi_search = fred.search('Consumer Price Index for All Urban Consumers: All Items in U.S. City Average')




#%%
