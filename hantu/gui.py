import tkinter as tk

# 종목 리스트를 입력받는 함수
def get_ticker_list():
    # 입력받은 종목 리스트를 저장할 리스트
    ticker_list = []

    # 종목 리스트를 입력받는 창 생성
    ticker_list_window = tk.Toplevel(window)
    ticker_list_window.title("Enter Ticker List")

    # 종목 리스트 입력받는 위젯 생성
    ticker_list_label = tk.Label(ticker_list_window, text="Enter Ticker List:")
    ticker_list_label.pack()

    ticker_list_entry = tk.Entry(ticker_list_window)
    ticker_list_entry.pack()

    # 종목 리스트 입력받는 함수
    def add_ticker_list():
        ticker_list.append(ticker_list_entry.get())
        ticker_list_entry.delete(0, tk.END)

    # 종목 추가 버튼 생성
    add_ticker_button = tk.Button(ticker_list_window, text="Add Ticker", command=add_ticker_list)
    add_ticker_button.pack()

    # 종목 리스트 저장 버튼 생성
    save_ticker_button = tk.Button(ticker_list_window, text="Save Ticker List", command=ticker_list_window.destroy)
    save_ticker_button.pack()

    # 종목 리스트 입력받는 창 실행
    ticker_list_window.mainloop()

    return ticker_list

# 종목 리스트 입력받기
ticker_list = get_ticker_list()