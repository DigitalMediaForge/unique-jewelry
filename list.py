from category import Category
from product import Product
from woocommerce import API

WOO_CONSUMER_KEY="ck_b8907c3d0ffa8ec68435bcd62e02c9520ec2bbce"
WOO_PRIVATE_KEY="cs_87a874f6e6d77a3481fdb4bae7a3cd160f1945ab"

wcapi = API(
    url="https://uniquejewelry.pl",
    consumer_key=WOO_CONSUMER_KEY,
    consumer_secret=WOO_PRIVATE_KEY,
    wp_api=True,
    version="wc/v3",
    query_string_auth=True
)

try:
    product_object = Product(wcapi)
    product_object.get_all()
except:
    print("Error")