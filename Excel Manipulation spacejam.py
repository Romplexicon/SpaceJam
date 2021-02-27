import datetime
from openpyxl import Workbook
from openpyxl import load_workbook
#wb=Workbook()
#No longer required after creation of excel sheet
wb = load_workbook('DataRepo.xlsx')
ws= wb.active
#Opens a sheet to start working on
ws.title="Input Data"
wb.save('DataRepo.xlsx')
flag=0
global count
count=1
#Format of Data Storage: Name, Severity, Location
class user:
    N= str()
    D= datetime.datetime(2020,1,1)
    #YY,MM,DD
    S= str()
    L= str()
    def input():
        N=input("Enter your name")
        D=input("Date tested")
        S=input("Calculated severity @Anish")
        L=input("Vector location @abhay")
#Works till here
'''
global U
U=user()
def write():
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
    wb.save('DataRepo.xlsx')

wb.save('DataRepo.xlsx')
#saves the data
'''
