import requests
import bs4
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/country/ukraine/'

page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')

cases = soup.find_all('div', class_='maincounter-number')

data = []

for i in cases:
    span = i.find('span')
    data.append(span.string)
    
# print(data)

df = pd.DataFrame({"Corona": data})

df.index = ['Total', 'Deaths', 'Recovered']

df.to_csv('corona.csv')