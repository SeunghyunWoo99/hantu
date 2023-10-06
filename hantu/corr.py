import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

from yahooquery import Ticker

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
queryParams = '?' + \
              'ServiceKey=' + 'I7nTXbi3PzfbHXhVxG7DlQOnGNstBL%2FrmkM%2FajUQuEsTsbfhhq1QJ%2BE7K8h54B2wiR2%2BJJmKk5fmoS5xsaahIw%3D%3D' + \
              '&pageNo='+ '1' + \
              '&numOfRows='+ '999' + \
              '&dataType='+ 'JSON' + \
              '&dataCd='+ 'ASOS' + \
              '&dateCd='+ 'DAY' + \
              '&startDt='+ '20230101' + \
              '&endDt='+ '20231004' + \
              '&stnIds='+ '108' # \

result = requests.get(url + queryParams)

js = json.loads(result.content)

weather_data = pd.DataFrame(js['response']['body']['items']['item'])
weather_data.to_excel('weather_data.xlsx', index=False)

# 'avgTca' 열의 이름을 'temp'로 변경합니다.
weather_data = weather_data.rename(columns={'avgTca': 'weather'})

weather_data = weather_data[['tm', 'weather']]

# 'tm' 열을 datetime 형식으로 변환합니다.
weather_data['tm'] = pd.to_datetime(weather_data['tm'], format='%Y-%m-%d')

# 시작 날짜와 끝 날짜를 입력받습니다.
start_date = '2023-01-01'
end_date = '2023-10-04'



# Yahoo Finance에서 KOSPI 지수 데이터를 가져옵니다.
ticker = Ticker('^KS11')
kospi_data = ticker.history(start=start_date, end=end_date)

# 'adjclose' 열의 이름을 'temp'로 변경합니다.
kospi_data = kospi_data.rename(columns={'adjclose': 'kospi'})

# 'date' 열을 datetime 형식으로 변환합니다.
kospi_data = kospi_data.reset_index().set_index('date')
kospi_data.index = pd.DatetimeIndex(kospi_data.index)
kospi_data.index = kospi_data.index.tz_localize(None)
kospi_data.index = pd.to_datetime(kospi_data.index)

print(weather_data)
print(kospi_data)

# 기상 데이터와 주식 데이터를 합칩니다.
merged_data = pd.merge(weather_data, kospi_data, left_on='tm', right_on=kospi_data.index, how='inner')
merged_data.to_excel('merged_data.xlsx', index=False)

print(merged_data)
print(merged_data[['weather', 'kospi']])
# 'temp' 열과 'temp' 열 간의 상관관계를 구합니다.
corr = merged_data[['weather', 'kospi']].corr()

# 상관관계를 출력합니다.
print(corr)

# 그래프를 그립니다.
ax = merged_data.plot(x='tm', y='weather', figsize=(12,6), color='blue')
merged_data.plot(x='tm', y='kospi', secondary_y=True, ax=ax, color='red')
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title(f"Weather vs Kospi")
plt.show()

# 산점도 그래프를 그립니다.
plt.scatter(merged_data['weather'], merged_data["kospi"])
plt.xlabel('Kospi')
plt.ylabel("Weather")
plt.show()
