from yahooquery import Ticker
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import filedialog

# select_folder_path 함수를 정의합니다.
def select_folder_path():
    # 폴더 대화상자를 열어 폴더 경로를 선택합니다.
    folder_path = filedialog.askdirectory(initialdir="./")

    # 선택한 폴더 경로를 출력합니다.
    print(folder_path)

    # 선택한 폴더 경로를 path_entry 위젯에 출력합니다.
    path_entry.config(state="normal")
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_path)
    path_entry.config(state="disabled")

def export_to_excel():
    # 시작 날짜, 끝 날짜, 그리고 엑셀 파일 이름을 입력받습니다.
    start_date = start_date_entry.get_date().strftime('%Y-%m-%d')
    end_date = end_date_entry.get_date().strftime('%Y-%m-%d')
    
    file_name = (path_entry.get() or ".") + "/" + (file_name_entry.get() or "data") + ".xlsx"
    
    
    # Yahoo Finance에서 주식 데이터를 가져옵니다.
    ticker_symbol = stock_code_entry.get()
    ticker = Ticker(ticker_symbol)
    stock_data = ticker.history(start=start_date, end=end_date)

    # 데이터프레임의 인덱스를 날짜로 설정합니다.
    stock_data = stock_data.reset_index().set_index('date')
    
    # 인덱스를 DatetimeIndex로 변환합니다.
    stock_data.index = pd.DatetimeIndex(stock_data.index)

    # 인덱스의 타임존 정보를 제거합니다.
    stock_data.index = stock_data.index.tz_localize(None)

    # 데이터프레임을 엑셀 파일로 저장합니다.
    stock_data.to_excel(file_name, sheet_name=ticker_symbol)

    # 데이터 종류 이름을 추출합니다.
    data_columns = stock_data.columns.tolist()

    # 첫 번째 행에 데이터 종류 이름을 추가합니다.
    data_columns.insert(0, "Data Type")

    # 첫 번째 열에 날짜를 추가합니다.
    stock_data.insert(0, "Date", pd.to_datetime(stock_data.index).strftime('%Y-%m-%d'))

    # 데이터 종류 이름을 첫 번째 행에 추가합니다.
    stock_data.columns = data_columns

    # 데이터프레임을 엑셀 파일로 다시 저장합니다.
    stock_data.to_excel(file_name, sheet_name=ticker_symbol, index=False)

    # 메시지 박스를 열어서 저장이 완료되었음을 알립니다.
    messagebox.showinfo("저장 완료", "엑셀 변환이 성공적으로 완료되었습니다.")

def search_data():
    # 시작 날짜와 끝 날짜를 입력받습니다.
    start_date = start_date_entry.get_date().strftime('%Y-%m-%d')
    end_date = end_date_entry.get_date().strftime('%Y-%m-%d')

    # Yahoo Finance에서 AAPL 주식 데이터를 가져옵니다.
    ticker = Ticker(stock_code_entry.get())
    stock_data = ticker.history(start=start_date, end=end_date)

    # 데이터프레임의 인덱스를 날짜로 설정합니다.
    stock_data = stock_data.reset_index().set_index('date')

    # treeview에 데이터를 추가합니다.
    for index, row in stock_data.iterrows():
        treeview.insert("", "end", values=[index.strftime('%Y-%m-%d')] + list(row))
    
def print_input():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    file_name = (path_entry.get() or "./") + (file_name_entry.get() or "data") + ".xlsx"

    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"File Name: {file_name}")

# tkinter 윈도우를 생성합니다.
window = tk.Tk()
window.title("Yahoo Finance")

# 조회 프레임 (entry, 검색버튼, 엑셀 버튼)
search_frame = tk.Frame(window)
search_frame.pack(expand=True, pady=10,fill="both")

# 종목 코드 입력
stock_code_label = tk.Label(search_frame, text="Stock Code:")
stock_code_label.pack(side="left", padx=5, fill="both")
stock_code_entry = tk.Entry(search_frame)
stock_code_entry.pack(side="left", padx=5, fill="both")

# 시작 날짜를 입력받는 레이블과 DateEntry 위젯을 생성합니다.
start_date_label = tk.Label(search_frame, text="Start Date:")
start_date_label.pack(side="left", padx=5, fill="both")
start_date_entry = DateEntry(search_frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
start_date_entry.pack(side="left", padx=5, fill="both")

# 끝 날짜를 입력받는 레이블과 DateEntry 위젯을 생성합니다.
end_date_label = tk.Label(search_frame, text="End Date:")
end_date_label.pack(side="left", padx=5, fill="both")
end_date_entry = DateEntry(search_frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
end_date_entry.pack(side="left", padx=5, fill="both")

# 조회 버튼을 생성합니다.
search_button = tk.Button(search_frame, text="Search", command=search_data)
search_button.pack(side="left", padx=5, fill="both")




# 조회 프레임 (entry, 검색버튼, 엑셀 버튼)
export_frame = tk.Frame(window)
export_frame.pack(expand=True, pady=10,fill="both")


# 엑셀 파일 이름을 입력받는 레이블과 엔트리 위젯을 생성합니다.
file_name_label = tk.Label(export_frame, text="Excel File Name:")
file_name_label.pack(side="left", padx=5, fill="both")
file_name_entry = tk.Entry(export_frame)
file_name_entry.pack(side="left", padx=5, fill="both")



# Path 라벨과 path_entry 위젯을 생성합니다.
path_label = tk.Label(export_frame, text="Path:")
path_label.pack(side="left", padx=5, fill="both")
path_entry = tk.Entry(export_frame, state="disabled")
path_entry.pack(side="left", padx=5, fill="both")
# 폴더 선택 버튼을 생성합니다.
select_folder_button = tk.Button(export_frame, text="Select Folder", command=select_folder_path)
select_folder_button.pack(side="left", padx=5, fill="both")

# 엑셀로 export하는 버튼을 생성합니다.
export_button = tk.Button(export_frame, text="Export to Excel", command=export_to_excel)
export_button.pack(side="left", padx=5, fill="both")

# 확인 버튼을 생성합니다.
confirm_button = tk.Button(window, text="Print", command=print_input)
confirm_button.pack(expand=True, pady=10,fill="both")



treeFrame = tk.Frame(window)
treeFrame.pack(side="top", fill="both")
treeScroll = tk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("open", "high", "low", "close", "volume", "adjclose", "dividends")
treeview = tk.ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=13)

treeview.column("open", width=100)
treeview.heading("open", text="open")
treeview.column("high", width=100)
treeview.heading("high", text="high")
treeview.column("low", width=100)
treeview.heading("low", text="low")
treeview.column("close", width=100)
treeview.heading("close", text="close")
treeview.column("volume", width=100)
treeview.heading("volume", text="volume")
treeview.column("adjclose", width=100)
treeview.heading("adjclose", text="adjclose")
treeview.column("dividends", width=100)
treeview.heading("dividends", text="dividends")

treeview.pack()
treeScroll.config(command=treeview.yview)



# tkinter 윈도우를 실행합니다.
window.mainloop()