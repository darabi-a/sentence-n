from customtkinter import *


#تابع محاسبات
def Operation():
    #گرفتن اطلاعات و تبدیل به لیست
    sequence = list(input_.get())
    # حذف فاصله‌ها از لیست
    sequence = [x for x in sequence if x != " "]
    # تبدیل اعضای لیست به نوع داده‌ای int
    sequence = list(map(int, sequence))

    a1 = sequence[0]
    a2 = sequence[1]
    a3 = sequence[2]
    # انجام محاسبات
    x1 = a1 + a3
    x2 = a2 * 2
    # بررسی برابری x1 و x2 و محاسبه d
    if x1 == x2:
        d = a2 - a1
        answer.configure(text=f"tn = {a1} + (n-1) * {d}")
    else:
        answer.configure(text="Your sequence does not count")
        
        
        
#ساخت یک پنجره
win = CTk()
#تایتل پنجره
win.title("sentence n")
#بخش اندازه پنجره
win.geometry("330x200")
win.maxsize(330, 200)
win.minsize(330, 200)
#متن راهنما
guide = CTkLabel(win, text="guide: Separate consecutive sentences with space.", font=CTkFont(size=14))
guide.pack(pady=(5,0))
#بخش input
input_= CTkEntry(win, 240, 35, font=CTkFont(size=16),placeholder_text="Enter your sequence:")
input_.pack(pady=(10,5))
#دکمه ارسال اطلاعات
submit = CTkButton(win, 70, 35,text="submit",font=CTkFont(size=16), corner_radius=12, command=Operation)
submit.pack()
#بخش نشان دهنده جواب
answer = CTkLabel(win, 240, 40, text=" ",font=CTkFont(size=20))
answer.pack(pady=10)
#اجرا پنجره
win.mainloop()
