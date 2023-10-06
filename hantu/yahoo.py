from yahooquery import Ticker
import matplotlib.pyplot as plt



# 시작 날짜와 끝 날짜를 입력받습니다.
start_date = '2023-01-01'
end_date = '2023-12-31'

# Yahoo Finance에서 AAPL 주식 데이터를 가져옵니다.
ticker = Ticker('^KS11')
kospi_data = ticker.history(start=start_date, end=end_date)

# 데이터프레임의 인덱스를 날짜로 설정합니다.
kospi_data = kospi_data.reset_index().set_index('date')

plt.plot(kospi_data.index, kospi_data['close'])
plt.xlabel('Date')
plt.ylabel('KOSPI Index')
plt.title('KOSPI Index in 2020')
plt.show()
