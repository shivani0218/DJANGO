from faker import  Faker
from myapi.models import Product
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

fakegen = Faker()

def PopulateOrders():
    Order1 = Product(
        product_name='BAG',
        brand='ZARA',
        discount_amt='4999',
        purchase_price='3999',
        product_description='High Quality LEATHER BAG.',
        product_status=''
                    )
    Order2 = Product(
        product_name='GOGGLES',
        brand='ZARA',
        discount_amt='4999',
        purchase_price='3999',
        product_description='High Quality Frames.',
        product_status=''
    )
    Order1.save()
    Order2.save()
    print("Finished..products populated")

if __name__ == "__main__":
    PopulateOrders()