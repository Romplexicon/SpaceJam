from openpyxl import Workbook
from openpyxl import load_workbook
wb = load_workbook('DataRepo.xlsx')
ws= wb.active
#Opens a sheet to start working on
ws.title="Input Data"
flag=0
global count
count=1
#Format of Data Storage: Name, Severity, Location
class user:
    N=input("Enter your name")
    D=input("Date tested")
    S=input("Calculated severity @Anish")
    L=input("Vector location @abhay")

global U
U=user()
while(flag!=1):
    #global count
    #global U
    SN=ws.cell(row=count,column=1)
    SN.value=U.N
    SD=ws.cell(row=count,column=2)
    SD.value=U.D
    SS=ws.cell(row=count,column=3)
    SS.value=U.S
    SL=ws.cell(row=count,column=4)
    SL.value=U.L
    count=count+1
    wb.save('DataRepo.xlsx')

wb.save('DataRepo.xlsx')
#saves the data
