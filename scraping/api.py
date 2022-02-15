import json
import requests

url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5' 

def load_ex():
    return json.loads(requests.get(url).text)

def get_ex(ccy):
    for exc in load_ex():
        if ccy == exc['ccy']:
            return exc
        return False
    
ex_now = get_ex('USD')
print(ex_now)