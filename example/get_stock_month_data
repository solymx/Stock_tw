# 會獲取該當月的所有資料
```
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
```
