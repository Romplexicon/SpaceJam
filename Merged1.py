from datetime import date
from openpyxl import Workbook, load_workbook

# wb=Workbook()
# No longer required after creation of excel sheet
wb = load_workbook('DataRepo.xlsx')
ws = wb.active
# Opens a sheet to start working on
ws.title = "Input Data"
wb.save('DataRepo.xlsx')
flag = 0
global count
count = 1
global count_positive
count_positive = 0
global High_Risk_Sections
High_Risk_Sections = []


class severity():
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    d = d1.split("/")
    status = ""
    str = ""
    test = input("Please enter if you tested negative for covid 19 after testing positive : ")
    for i in d:
        str += i
    try:
        date_all = int(str)
    except:
        print("Found an error in time..Cannot continue")
    print(f"Today's date is {d1}")
    D2 = input("Please enter the date you last tested negative for Covid-19. Enter in the form of YY/MM/DD : ")
    d2 = D2.split("/")
    str2 = ""
    for i in d2:
        str2 += i
        date_test = int(str2)
    f_date = date(int(d[0]), int(d[1]), int(d[2]))
    l_date = date(int(d2[0]), int(d2[1]), int(d2[2]))
    delta = f_date - l_date
    x = delta.days
    #Risk period 3 months
    if x >= 90:
        status = "High Risk"
    elif x>90 and x<180:
        status="Medium Risk"
    else:
        status = "Low Risk"

a = severity()


# Format of Data Storage: Name, Severity, Location
class user:
    global N, D, S, C #L
    N = str()
    S = severity()
    #L = str()
    C = str()

    def input(self):
        global N, D, S, L
        N = input("Enter your name : ")
        C = input("Enter your section : ")
        D = a.D2
        S = a.status
        #L = input("Vector location @abhay")
        if S == "High Risk":
            High_Risk_Sections.append(C)
        print(High_Risk_Sections)


global U
U = user()
U.input()  # This inputs


# Function to write
def write():
    SN = ws.cell(row=count, column=1)
    SN.value = N
    SD = ws.cell(row=count, column=2)
    SD.value = D
    SS = ws.cell(row=count, column=3)
    SS.value = S
    #SL = ws.cell(row=count, column=4)
    #SL.value = L
    SC = ws.cell(row=count, column=5)
    SC.value = C
    wb.save('DataRepo.xlsx')


write()
# Function to read
def read():
    SN = ws.cell(row=count, column=1)
    N = SN.value
    SD = ws.cell(row=count, column=2)
    D = SD.value
    SS = ws.cell(row=count, column=3)
    S = SS.value
    #SL = ws.cell(row=count, column=4)
    #L = SL.value


# function usage

write()
read()
