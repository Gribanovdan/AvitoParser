import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active


print(sheet.selected_cell)
wb.save('test.xlsx')