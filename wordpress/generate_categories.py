import csv
import requests
import os
from category import Category
from product import Product
from woocommerce import API

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WOO_CONSUMER_KEY="ck_b8907c3d0ffa8ec68435bcd62e02c9520ec2bbce"
WOO_PRIVATE_KEY="cs_87a874f6e6d77a3481fdb4bae7a3cd160f1945ab"

wcapi = API(
    url="https://uniquejewelry.pl",
    consumer_key=WOO_CONSUMER_KEY,
    consumer_secret=WOO_PRIVATE_KEY,
    wp_api=True,
    version="wc/v3"
)

categoryObject = Category(wcapi)
categoryList = []

with open('download.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: line_count += 1
        else:
            if len(row) > 15: 
                image = row[15]
                short = image.replace('https://drop.seltu.pl/', '')

                if len(short) != 0:
                    categoryList = categoryList + row[8].split(' > ')

            line_count += 1
    print(f'Processed {line_count} lines.')

categoryList = list(dict.fromkeys(categoryList))
for categoryName in categoryList:
    categoryObject.create_new(categoryName)

print(categoryList)





