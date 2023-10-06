from tkinter import*
import requests
from bs4 import BeautifulSoup
 
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj
#bs_obj를 받아서 price를 return
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text
 
#company_codes = ["005930","000660"]
def get_Price_from_ent():
    f = ent.get();
 
    lbl_2.configure(text = str(get_price(f)))
    return
 
root = Tk()
root.title("Stock Program ")
root.geometry("540x280")
 
 
lbl_1 = Label(root, text = "Company Number")
ent = Entry(root)
lbl_2 = Label(root, text = "0")
btn = Button(root, text = "Search", command = get_Price_from_ent)
 
lbl_1.place(x = 20, y = 30)
ent.place(x = 150, y = 30)
btn.place(x = 150, y = 70)
lbl_2.place(x = 150, y = 120)
 
sg_condition_frame = Frame(root)
sg_condition_frame.pack(side="top", pady=20,fill="both")

frame_middle_left = LabelFrame(sg_condition_frame, text="상가 구분")
frame_middle_left.pack(side="left", fill="both", expand=True)

sg_chk1 = IntVar()
sg_chk1_box = Checkbutton(frame_middle_left, text="상가", variable = sg_chk1)# 상가
sg_chk1_box.pack(side="left")
sg_chk1_box.select()

sg_chk2 = IntVar()
sg_chk2_box = Checkbutton(frame_middle_left, text="상가주택", variable = sg_chk2)# 상가주택
sg_chk2_box.pack(side="left")
 
root.mainloop()
