import csv
import requests
import os

from converters.colibra_product import ColibraProduct
from entities.colibra_category_parser import ColibraCategoryParser
from entities.image import LowQualityImages
from entities.shopify_product import ShopifyProduct
from support.shopify_csv import ShopifyCSV

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_WIHOUT_IMAGES = [3239, 3951, 4100, 4116, 4596, 5032, 5176]

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

def is_ignored(product: ColibraProduct):
    if int(product.productId) in CONTENT_WIHOUT_IMAGES: 
        return 1
    else: 
        return 0
    
counter = LowQualityImages()
with open('download_eur.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    
    rowsCollection = []
    for row in csv_reader:
        colibra = ColibraProduct(row)

        if line_count == 0: 
            line_count += 1
        elif is_ignored(colibra) == 0 and colibra.img1 != '':
            colibra: ColibraProduct = counter.filterLowQualityImages(colibra)
            
            categorySamples = ColibraCategoryParser(colibra.category)
            shopifyProduct = ShopifyProduct()
            rows = shopifyProduct.createRows(product=colibra, category=categorySamples)
            rowsCollection = rowsCollection + rows

            print('process: ' + str(line_count))
            line_count += 1
        else:
            line_count += 1


targetCsv = ShopifyCSV()
targetCsv.addData(rowsCollection)



print(f'Processed {line_count} lines.')

print(counter.getCsvSkipped())
    