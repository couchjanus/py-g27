import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = []

# print(page.text)

data_iter = iter(soup.find_all('td'))

while True:
    try:
        country = next(data_iter).text
        confirmed = next(data_iter).text
        deaths = next(data_iter).text
        continent = next(data_iter).text
        
        data.append((
            country, 
            int(confirmed.replace(' ', '').replace(',', '')),
            int(deaths.replace(' ', '').replace(',', '')),
            continent
        ))
    except StopIteration:
        break
    
print(data)