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

# Yahoo Finance에서 AAPL 주식 데이터를 가져옵니다.
ticker = Ticker('^KS11')
kospi_data = ticker.history(start=start_date, end=end_date)

# 데이터프레임의 인덱스를 날짜로 설정합니다.
kospi_data = kospi_data.reset_index().set_index('date')

