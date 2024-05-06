import yfinance as yf
import requests
import pandas as pd
import datetime as dt


stock_id = '2330.TW'

end = dt.date.today() # today is end
start = end - dt.timedelta(days = 360)

stock_data = yf.download(stock_id, start=start, end=end)
stock_data.tail()
"""
output:
             
Date        Open   High    Low   Close  Adj Close    Volume
2024-04-26  788.0  789.0  782.0  782.0      782.0  32571247
2024-04-29  790.0  795.0  787.0  795.0      795.0  26765837
2024-04-30  797.0  802.0  790.0  790.0      790.0  39051972
2024-05-02  789.0  789.0  772.0  772.0      772.0  40527228
2024-05-03  788.0  788.0  773.0  780.0      780.0  29901556

"""
