import scrapy
import csv


with open('../../config.csv', 'r', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    data = []
    for line in reader:
        data.append(line)


class PricesSpider(scrapy.Spider):
    name = 'prices'
    start_urls = [line[0] for line in data]

    def parse(self, response):
        response.xpath()