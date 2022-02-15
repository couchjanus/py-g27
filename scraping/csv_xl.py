import csv
import openpyxl

def csv_to_excel(csv_file, excel_file):
    csv_data = []
    with open(csv_file) as f:
        reader = csv.reader(f)
        for r in reader:
            csv_data.append(r)
            
        wb = openpyxl.Workbook()
        sheet = wb.active
        for r in csv_data:
            sheet.append(r)
        wb.save(excel_file)
        
if __name__ == '__main__':
    csv_to_excel('emploeys.csv', 'book.xlsx')
        
    