from openpyxl import Workbook
wb= load_workbook('DataRepo.xlsx')
ws= wb.active
#Opens a sheet to start working on
ws.title="Input Data"
wb.save('DataRepo.xlsx')
#saves the data
flag=0
#Format of Data Storage: Name, Severity, Location
class user:
    N=input("Enter your name")
    S=input("Calculated severity @Anish")
    L=input("Vector location @abhay")
    
while(flag!=1):
    
