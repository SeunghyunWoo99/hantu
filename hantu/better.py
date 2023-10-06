from fredapi import Fred
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr

fred = Fred(api_key='d6884c99ffc6141922be1b794d79edbb')
start_date = '2014-01-01'
end_date = '2024-12-31'
unrate_series = fred.get_series('UNRATE', observation_start=start_date, observation_end=end_date)
sp500_series = fred.get_series('SP500', observation_start=start_date, observation_end=end_date)

# 두 데이터의 인덱스를 비교하여 겹치는 기간에 대해서만 값을 비교
unrate_series = unrate_series[sp500_series.index[0]:sp500_series.index[-1]]
sp500_series = sp500_series[unrate_series.index[0]:unrate_series.index[-1]]

# 누락된 값을 보간하여 채워줌
unrate_series = unrate_series.interpolate()
sp500_series = sp500_series.interpolate()

# 두 데이터를 concatenate() 함수를 사용하여 연결
# data_vector = np.concatenate((unrate_series.values.reshape(-1, 1), sp500_series.values.reshape(-1, 1)), axis=1)
# cosine_sim = cosine_similarity(data_vector)

# print(cosine_sim)

# 두 데이터 간의 Pearson 상관계수 계산
# corr, _ = pearsonr(unrate_series, sp500_series)

# print('Pearson correlation coefficient: %.3f' % corr)

# 그래프 그리기
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(unrate_series)
ax1.set_title('Unemployment Rate')
ax1.set_xlabel('Date')
ax1.set_ylabel('Rate')

ax2.plot(sp500_series)
ax2.set_title('S&P 500')
ax2.set_xlabel('Date')
ax2.set_ylabel('Price')

plt.show()