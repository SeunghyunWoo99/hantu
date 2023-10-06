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

weather_data = weather_data[['tm', 'avgTca']]

# 데이터프레임을 엑셀 파일로 저장합니다.
weather_data.to_excel('weather_data.xlsx', index=False)

# 'tm' 열을 datetime 형식으로 변환합니다.
weather_data['tm'] = pd.to_datetime(weather_data['tm'], format='%Y-%m-%d')

# 시작 날짜와 끝 날짜를 입력받습니다.
start_date = '2023-01-01'
end_date = '2023-12-31'

# Yahoo Finance에서 KOSPI 지수 데이터를 가져옵니다.
ticker = Ticker('^KS11')
kospi_data = ticker.history(start=start_date, end=end_date)

# 데이터프레임의 인덱스를 날짜로 설정합니다.
kospi_data = kospi_data.reset_index().set_index('date')
kospi_data.to_excel('kospi_data.xlsx', index=False)

# 그래프를 그립니다.
fig, ax1 = plt.subplots(figsize=(15, 9))

# 첫 번째 축을 설정합니다.
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Cloud Cover', color=color)
ax1.plot(weather_data['tm'], weather_data['avgTca'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# 두 번째 축을 설정합니다.
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('KOSPI Index', color=color)
ax2.plot(kospi_data.index, kospi_data['close'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# 첫 번째 축의 눈금을 조정합니다.
ax1.xaxis.set_major_locator(plt.MaxNLocator(5.0))

# 그래프의 제목을 설정합니다.
plt.title('Cloud Cover and KOSPI Index in 2023')

# 그래프를 출력합니다.
plt.show()


