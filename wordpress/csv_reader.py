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

category_object = Category(wcapi)
product_object = Product(wcapi)

def download_file(product_id, image_url):
    img_data = requests.get(image_url).content
    with open(ROOT_DIR + '/images/' + product_id + '.jpg', 'wb') as handler:
        handler.write(img_data)

def get_all_images_from_csv_row(row, firstPosition = 15):
    imageList = []
    for i in range(firstPosition,len(row),1):
        image = row[i]
        if len(image.replace('https://drop.seltu.pl/', '')) != 0:
            imageList.append(row[i])

    return imageList

def create_product(row):
    if len(row) > 15: 
        image = row[15]
        short = image.replace('https://drop.seltu.pl/', '')

        if len(short) != 0:
            categories = category_object.retrieve_category_ids(row[8])

            print('CATEGORIES')
            print(categories)


            images = get_all_images_from_csv_row(row)     
            product_code = row[1]       

            body = product_object.body(product_code, row[3], row[4], row[12], images, categories)
            ## Uncomment to post data
            product_object.create(body)
            print('The product ID: ' + str(row[0]) + ' was already processed')
            print(body)

            ## Uncomment to download images
            # download_file(row[0], image)

with open('download.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: 
            line_count += 1
        elif line_count in range(1, 10, 1): ## <-- THIS ONE WAS NOT PROCESSED
        # elif line_count in range(11, 100, 1):
        # elif line_count in range(101, 200, 1): 
        # elif line_count in range(201, 1000, 1):
        # elif line_count in range(1001, 2000, 1):
        # elif line_count in range(2001, 3000, 1):
        # elif line_count in range(3001, 3031, 1):
            create_product(row)
            print('process: ' + str(line_count))
            line_count += 1
        else:
            line_count += 1

    print(f'Processed {line_count} lines.')

    # NEXT: 101
    # END: 3031






