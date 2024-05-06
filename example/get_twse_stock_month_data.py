# 會獲取該當月的所有資料
# 一直連續抓可能會被 ban , maybe 50 次
import requests
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta 

stock_id = '2330'

# get today time , example: 20240506
date = dt.date.today().strftime("%Y%m%d")

# get taiwan stokc website information
stock_data = requests.get(f'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={date}&stockNo={stock_id}')

json_data = stock_data.json()
df = pd.DataFrame(data=json_data['data'], columns=json_data['fields'])

df.tail()

###
"""
output
          日期        成交股數            成交金額     開盤價     最高價     最低價     收盤價    漲跌價差    成交筆數
          0  113/05/02  47,536,363  36,983,047,647  789.00  789.00  772.00  772.00  -18.00  85,051
          1  113/05/03  31,026,748  24,240,817,990  788.00  788.00  773.00  780.00   +8.00  35,153

"""
