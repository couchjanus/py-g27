
from asyncio import DatagramTransport
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv


url = 'https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets'

fl = 'music4.csv'
f = open(fl, 'w', newline='')
writer = csv.writer(f)


page = requests.get(url)
# print(page.text)
soup = bs(page.text, 'html.parser')

table = soup.find_all('table',class_='wikitable plainrowheaders sortable')[4]

cases = table.find_all('tr')

data = []

for i in cases:
    cols = i.findChildren(recursive = False)
    cols = [elem.text.strip() for elem in cols]
    writer.writerow(cols)
    data.append(cols)
    
df = pd.DataFrame(data = data[1:], columns=data[3])

df.to_excel('music4.xlsx', index=False, header=False)