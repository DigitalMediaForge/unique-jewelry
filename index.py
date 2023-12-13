import os
from category import Category
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
cats = categoryObject.get_all_static()

print(cats)