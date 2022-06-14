from faker import  Faker
from myapi.models import Product
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

fakegen = Faker()

def PopulateProducts():
    product1 = Product(
              product_name = fakegen.commerce.product(),
              brand = 'GUCCI',
              product_max_price = '4999',
              product_discount_price='3999',
              product_description='High Quality Leather bag',
              product_long_description ='',
              in_stock_total ='5'
                    )
    product2 = Product(
        product_name='GOGGLES',
        brand='ZARA',
        product_max_price='4999',
        product_discount_price='3999',
        product_description='High Quality Frames.',
        product_long_description='',
        in_stock_total='5'
    )
    product1.save()
    product2.save()
    print("Finished..products populated")

if __name__ == "__main__":
    PopulateProducts()