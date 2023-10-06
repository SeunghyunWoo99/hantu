from fredapi import Fred
import pandas as pd

def save_fred_data_to_excel(series_id_list, start_date, end_date):
    # FRED에서 데이터를 가져옵니다.
    fred = Fred(api_key='d6884c99ffc6141922be1b794d79edbb')
    fred_data = pd.DataFrame()
    for series_id in series_id_list:
        data = fred.get_series(series_id, start_date=start_date, end_date=end_date)
        fred_data[series_id] = data

    # 데이터프레임의 인덱스를 날짜로 설정합니다.
    fred_data.index.name = "Date"

    # 엑셀 파일 이름을 설정합니다.
    file_name = "fred_data.xlsx"

    # 데이터프레임을 엑셀 파일로 저장합니다.
    with pd.ExcelWriter(file_name) as writer:
        fred_data.to_excel(writer, sheet_name="FRED Data")

    # 데이터 종류 이름을 추출합니다.
    data_columns = fred_data.columns.tolist()

    # 첫 번째 행에 데이터 종류 이름을 추가합니다.
    data_columns.insert(0, "Data Type")

    # 첫 번째 열에 날짜를 추가합니다.
    fred_data.insert(0, "Date", fred_data.index)

    # 데이터 종류 이름을 첫 번째 행에 추가합니다.
    fred_data.columns = data_columns

    # 데이터프레임을 엑셀 파일로 다시 저장합니다.
    with pd.ExcelWriter(file_name) as writer:
        fred_data.to_excel(writer, sheet_name="FRED Data", index=False)

# series_id_list에 있는 데이터에 대해 데이터를 추출합니다.
series_id_list = ['UNRATE', 'SP500', 'GDP']
start_date = "2023-01-01"
end_date = "2023-09-25"

# ExcelWriter 객체를 생성합니다.
with pd.ExcelWriter('fred_data.xlsx') as writer:
    # series_id_list에 있는 데이터에 대해 데이터를 추출하고, 데이터프레임을 엑셀 파일에 저장합니다.
    save_fred_data_to_excel(series_id_list, start_date, end_date)