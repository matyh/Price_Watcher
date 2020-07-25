import lxml.html
import requests
import csv
import bs4
from price_parser import Price
import pandas as pd

eur_czk_rate = 26.25

# load data into df
data_df = pd.read_csv('config.csv', delimiter=',', header=0)

url = data_df['url']
price_selector = data_df['price_selector']
name_selector = data_df['name']

for u, p, n in zip(url, price_selector, name_selector):
    page = requests.get(u)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    name = n

    price = soup.select(p)
    if len(price) > 1 and not all([p == price[0] for p in price]):
        # following is for debugging
        print(u)
        for i in price:
            print(i)
        #
        raise ValueError("Multiple results")
    else:
        result = price[0].get('content')
        if result is None:
            result = price[0].get('data-price')

    print(f'{name:<30} {result}')
