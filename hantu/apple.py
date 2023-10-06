# 한 종목에 관한 데이터 추출

from yahooquery import Ticker
import pandas as pd

aapl = Ticker('aapl')

content_list= [
'asset_profile',
'calendar_events',
'company_officers',
'earning_history',
'earnings',
'earnings_trend',
'esg_scores',
'financial_data',
# 'fund_bond_holdings',
# 'fund_bond_ratings',
# 'fund_equity_holdings',
# 'fund_holding_info',
# 'fund_ownership',
# 'fund_performance',
# 'fund_profile',
# 'fund_sector_weightings',
# 'fund_top_holdings',
'grading_history',
'index_trend',
'industry_trend',
'insider_holders',
'insider_transactions',
]

data = []

for content in content_list:
    data.append(aapl.asset_profile)
    data.append(aapl.calendar_events)
    data.append(aapl.company_officers)
    data.append(aapl.earning_history)
    data.append(aapl.earnings)
    data.append(aapl.earnings_trend)
    data.append(aapl.esg_scores)
    data.append(aapl.financial_data)
    # data.append(aapl.fund_bond_holdings)
    # data.append(aapl.fund_bond_ratings)
    # data.append(aapl.fund_equity_holdings)
    # data.append(aapl.fund_holding_info)
    # data.append(aapl.fund_ownership)
    # data.append(aapl.fund_performance)
    # data.append(aapl.fund_profile)
    # data.append(aapl.fund_sector_weightings)
    # data.append(aapl.fund_top_holdings)
    data.append(aapl.grading_history)
    data.append(aapl.index_trend)
    data.append(aapl.industry_trend)
    data.append(aapl.insider_holders)
    data.append(aapl.insider_transactions)

df = pd.DataFrame(data, index=content_list)
df.to_excel('aapl.xlsx', index=False)
# df.to_excel('aapl.xlsx', index=True)