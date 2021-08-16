import pandas as pd
import sys
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

#lets creat a data dictionary
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(type(df))
#----------------------------------------------------------
#REST APIS
#Rest API’s function by sending a request, the request is communicated via HTTP message.
# The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service or resource to perform. In a similar manner,
# API returns a response, via an HTTP message, this response is usually contained within a JSON.
cg= CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)
print(bitcoin_data)
print(type(bitcoin_data))
bitcoin_price_data = bitcoin_data['prices']
print(bitcoin_price_data[0:5])
#now lets put it in a dataframe
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
print(data)
#Now that we have the DataFrame we will convert the timestamp to datetime and save it as a column called Date.
# We will map our unix_to_datetime to each timestamp and convert it to a readable datetime.

data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
print(data.head(2))
#now
candlestick_data = data.groupby(data.date, as_index=False).agg({'Price': ['min', 'max', 'first', 'last']})
print(type(candlestick_data))
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()