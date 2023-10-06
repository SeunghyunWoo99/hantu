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
gdp_series = fred.get_series('GDP', observation_start=start_date, observation_end=end_date)

# 그래프 그리기
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

ax1.plot(unrate_series)
ax1.set_title('Unemployment Rate')
ax1.set_xlabel('Date')
ax1.set_ylabel('Rate')

ax2.plot(sp500_series)
ax2.set_title('S&P 500')
ax2.set_xlabel('Date')
ax2.set_ylabel('Price')

ax3.plot(gdp_series)
ax3.set_title('GDP')
ax3.set_xlabel('Date')
ax3.set_ylabel('Value')

plt.show()