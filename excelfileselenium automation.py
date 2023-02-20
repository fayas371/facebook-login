
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

#for changing the name of the column
sheet['A1'] = "Username"
sheet['B1'] = "password"

limits=int(input("Enter the limits"))
#for entering the values in excel
for i in range(1,limits):
    sheet["A"+str(i+1)]= input("Enter the username:")
    sheet["B"+str(i+1)]= input("Enter the password:")

#for saving the excel file
wb.save('password.xlsx')





