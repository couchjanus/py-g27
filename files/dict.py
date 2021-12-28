import csv

FILENAME = 'emploey.csv'

emploeys = [
    {'name': 'CAT', 'phone': 1234567, 'added': '2021-12-16'}, 
    {'name': 'Mary', 'phone': '5555555', 'added': '2021-12-21'},
    {'name': 'Tom', 'phone': 777777, 'added': '2021-12-16'}
]

# with open(FILENAME, 'w', newline='') as fh:
#     columns = ['name', 'phone', 'added']

#     writer = csv.DictWriter(fh, fieldnames = columns)
#     writer.writeheader()

#     writer.writerows(emploeys)

#     em = {'name': 'Bob', 'phone': 888888, 'added': '2021-12-28'}
#     writer.writerow(em)

with open(FILENAME, newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['name' ], ' => ', row['phone'])