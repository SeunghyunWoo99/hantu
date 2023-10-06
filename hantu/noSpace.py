import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import Ticker

tickers = Ticker('aapl nflx', asynchronous=True)
df = tickers.history()
print(df)
df["adjclose"].plot()
plt.xticks(rotation=90)
plt.show()

# 데이터프레임을 엑셀 파일로 저장합니다.
df.to_excel("/data/data.xlsx", index=False)