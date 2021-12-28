# csv

import csv

FILENAME = "users.csv"

users = [
    ['cat', '2222222', '2021-12-16'],
    ['tom', '1111111', '2021-12-16'],
    ['dog', '3333333', '2021-12-16'],
]


# with open(FILENAME, 'w', newline='') as fh:
#     writer = csv.writer(fh)
#     writer.writerows(users)

# with open(FILENAME, 'a', newline='') as fh:
#     writer = csv.writer(fh)
#     user = ['Mary', '112113111', '2021-12-28']
#     writer.writerow(user)

with open(FILENAME, newline='') as fh:
    reader = csv.reader(fh)
    for row in reader:
        print(row[0], ' - ', row[1], ' - ', row[2])