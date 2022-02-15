import openpyxl
import csv

excel = openpyxl.load_workbook('emploeys.xlsx')

sheet = excel.active

col = csv.writer(open('emploeys.csv', 'w', newline=''))

for r in sheet.rows:
    col.writerow([cell.value for cell in r])