from datetime import date


today = date.today()
d1 = today.strftime("%Y/%m/%d")
d = d1.split("/")
status = ""
str=""
for i in d:
    str += i
try:
    date_all= int(str)
except:
    print("Found an error in time..Cannot continue")
print(d1)

D = input("Date tested negative. Enter in the form of YY/MM/DD : ")
d2 = D.split("/")
str2 = ""
for i in d2:
    str2 +=i
    date_test = int(str2)
f_date = date(int(d[0]), int(d[1]), int(d[2]))
l_date = date(int(d2[0]), int(d2[1]), int(d2[2]))
delta = f_date - l_date
x = delta.days
if x >= 90:
    status = "High Risk"
else:
    status = "Low Risk"
print(status)
