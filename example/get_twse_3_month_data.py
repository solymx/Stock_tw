import requests
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta 


# get ? month
month_num = 3
date_now = dt.datetime.now()

# create date list
# example: Out[13]: ['20240501', '20240401', '20240301']
date_list = [(date_now - relativedelta(months=i)).replace(day=1).strftime('%Y%m%d') for i in range(month_num) ]

date_list.reverse()

all_df = pd.DataFrame()


stock_id = '2330'


# USE Loop to get month data 

for date in date_list:
    url = f'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={date}&stockNo={stock_id}'
    try:
        json_data = requests.get(url).json()
        df = pd.DataFrame(data = json_data['data'],
                          columns=json_data['fields'])
        all_df = pd.concat([all_df, df], ignore_index=True)
    except Exception as e:
        print(f"cannot get {date} data")

all_df.head()

"""
output:
          日期        成交股數            成交金額     開盤價     最高價     最低價     收盤價    漲跌價差     成交筆數
0  113/03/01  24,167,721  16,699,995,060  697.00  697.00  688.00  689.00   -1.00   26,282
1  113/03/04  97,210,112  69,868,348,694  714.00  725.00  711.00  725.00  +36.00  125,799
2  113/03/05  73,299,411  53,751,887,376  735.00  738.00  728.00  730.00   +5.00   69,851
3  113/03/06  52,464,833  38,203,868,985  718.00  738.00  717.00  735.00   +5.00   49,897
4  113/03/07  80,382,406  61,221,034,146  755.00  769.00  754.00  760.00  +25.00   96,348

"""
