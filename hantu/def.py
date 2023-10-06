# 필요한 라이브러리를 가져옵니다
from yahooquery import Ticker
import pandas as pd 


# Yahoo Finance API에서 데이터를 추출하는 함수를 정의합니다
def add_company(code):
    # 해당 회사 코드를 사용하여 Ticker 객체를 생성합니다
    company = Ticker(code)

    name = company.price[code]['shortName']
    industry = company.asset_profile[code]['industry']
    marketCap = company.summary_detail[code]['marketCap']
    currentPrice= company.financial_data[code]['currentPrice']
    summary = company.asset_profile[code]['longBusinessSummary']
    targetPrice = company.financial_data[code]['targetMeanPrice']

    per = company.summary_detail[code]['trailingPE']
    eps = company.key_stats[code]['trailingEps']
    pbr = company.key_stats[code]['priceToBook']

    # all_data에서 특정 데이터를 추출합니다.

    df_earnings = pd.DataFrame(company.earnings[code]['financialsChart']['yearly'])

    rev2021 = df_earnings.iloc[-2,1]
    rev2020 = df_earnings.iloc[-3,1]
    rev2019 = df_earnings.iloc[-4,1]

    ear2021 = df_earnings.iloc[-2,2]
    ear2020 = df_earnings.iloc[-3,2]
    ear2019 = df_earnings.iloc[-4,2]

    doc = {
    'code':code,
    'name':name,
    'industry':industry,
    'marketCap':marketCap/1000,
    'currentPrice':currentPrice,
    'targetPrice':targetPrice,
    'per':per,
    'eps':eps,
    'pbr':pbr,
    'rev2021':rev2021/1000,
    'rev2020':rev2020/1000,
    'rev2019':rev2019/1000,
    'ear2021':ear2021/1000,
    'ear2020':ear2020/1000,
    'ear2019':ear2019/1000,
    }
    return doc

# 회사 코드 리스트를 정의합니다
ticker_list = ['AAPL', 'ABNB', 'BIDU', 'META', 'GOOG', 'MSFT', 'TSLA', 'PYPL', 'NFLX', 'NVDA']

# 각 회사의 데이터를 추출하여 리스트에 저장합니다
data = []
for code in ticker_list:
    data.append(add_company(code))

# 데이터프레임으로 변환합니다
df = pd.DataFrame(data)

# 데이터프레임을 엑셀 파일로 저장합니다
df.to_excel('company_data.xlsx', index=False)