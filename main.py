import lxml.html
import requests
import csv
import bs4
from price_parser import Price
import pandas as pd

eur_czk_rate = 26.25

# load data into df
data_df = pd.read_csv('config.csv', delimiter=',', header=0)


class Bike(object):
    def __init__(self, brand, name, url, price_selector):
        self.brand = brand
        self.name = name
        self.url = url
        self.price_selector = price_selector

    def get_price(self):
        page = requests.get(self.url)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        price = soup.select(self.price_selector)
        if len(price) > 1 and not all([p == price[0] for p in price]):

            # for debugging
            print(self.url)
            for i in price:
                print(i)
            #

            raise ValueError("Multiple results")
        else:
            result = price[0].get('content')
            if result is None:
                result = price[0].get('data-price')
        return result


with open('config.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data_header = next(reader)
    assert data_header == ['brand', 'name', 'url', 'price_selector'], \
        "Wrong data order"

    data = []
    for line in reader:
        data.append(line)


bikes = []
for line in data:
    bike = Bike(*line)
    bikes.append(bike)

# print(bikes[6].get_price())
for bike in bikes:
    price = bike.get_price()
    print(f'{bike.brand:<10} {bike.name:<20} {price}')
