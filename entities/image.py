import csv
import requests

from converters.colibra_product import ColibraProduct

IMAGE_SIZE_LIMIT = 50000

class LowQualityImages:
    def __init__(self) -> None:
        self.count = 0
        self.items = []

    def __add(self): 
        self.count += 1

    def appendItem(self, productId, imageUrl):
        self.__add()
        self.items.append([self.count, productId, imageUrl])

    def getCsvSkipped(self):
        with open('skipped_images.csv', 'w', encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(['number', 'product_code','image_url'])
    
            for row in self.items:
                writer.writerow(row)
    
    def totalSkipped(self):
        return self.count
    
    def filterLowQualityImages(self, product: ColibraProduct) -> ColibraProduct:
        if product.img1 != '':
            imgData = requests.get(product.img1).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img1)
                product.img1 = ''

        if product.img2 != '':
            imgData = requests.get(product.img2).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img2)
                product.img2 = ''

        if product.img3 != '':
            imgData = requests.get(product.img3).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img3)
                product.img3 = ''

        if product.img4 != '':
            imgData = requests.get(product.img4).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img4)
                product.img4 = ''

        if product.img5 != '':
            imgData = requests.get(product.img5).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img5)
                product.img5 = ''

        if product.img6 != '':
            imgData = requests.get(product.img6).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img6)
                product.img6 = ''

        if product.img7 != '':
            imgData = requests.get(product.img7).content
            if len(imgData) <= IMAGE_SIZE_LIMIT:
                self.appendItem(product.productId, product.img7)
                product.img7 = ''

        return (product)