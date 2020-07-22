from bs4 import BeautifulSoup
import requests
from decimal import Decimal
import re


URL = 'https://www.canyon.com/cs-cz/mountain-bikes/trail-bikes/neuron/neuron-cf-8.0/2471.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, features='html.parser')
price_raw = soup.find('div', class_="productDescription__priceSale")
price = price_raw.text.strip()
price = re.sub(r'[^\d,]', '', price).replace(',', '.')
print(float(price))
