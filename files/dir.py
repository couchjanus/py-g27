import os
path = 'C:\Windows'
with os.scandir(path) as d:
    for entry in d:
        print(entry.name)