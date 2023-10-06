from yahooquery import Ticker
import matplotlib.pyplot as plt
import pandas as pd


# 두 회사의 데이터를 야후쿼리를 이용해 받아옵니다.

# 시작날짜와 마지막날짜를 지정합니다.
date_start = "2015-01-01"
date_end = "2022-12-31"

# 두 회사의 시작날짜와 마지막날짜에 해당하는 데이터를 불러옵니다.
aapl = Ticker("AAPL")
aapl_data = aapl.history(start=date_start, end=date_end)

# 이때 인덱스(기준점)으로 쓸데없이 잡혀있는 회사의 심볼(티커)값을 빼줍니다.
aapl_data = aapl_data.reset_index().drop('symbol', axis=1)

# 데이터프레임의 인덱스를 날짜로 설정합니다.
aapl_data = aapl_data.set_index('date')

df = pd.DataFrame(aapl_data)
df.to_excel('aapl.xlsx', index=True)
