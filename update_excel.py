from openpyxl import load_workbook
wb = load_workbook('python_excel.xlsx')
sheet= wb.active;

wb.save('python_excel.xlsx')
wb.close()