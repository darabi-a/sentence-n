#بخش گرفتن ورودی
print("guide: Separate consecutive sentences with space.")
sequence = list(input("Enter your sequence:"))

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
    print(f"tn = {a1} + (n-1) * {d}")
else:
    print("Your sequence does not count")
