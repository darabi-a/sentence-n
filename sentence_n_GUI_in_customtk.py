from customtkinter import *

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
submit = CTkButton(win, 70, 35,text="submit",font=CTkFont(size=16), corner_radius=12)
submit.pack()
#بخش نشان دهنده جواب
answer = CTkLabel(win, 240, 40, text=" ")
answer.pack(pady=10)
#اجرا پنجره
win.mainloop()
