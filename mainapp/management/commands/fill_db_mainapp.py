import json
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, f'{file_name}.json'),
              encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        # [ProductCategory.objects.create(**category) for category in categories]
        product_categories_obj = [ProductCategory(**category) for category in \
                                  categories]
        ProductCategory.objects.bulk_create(product_categories_obj)  # for
        # one request creat all objects from product_categories_obj

        products = load_from_json('products')
        Product.objects.all().delete()
        products_obj = []
        for product in products:
            category_name = product['category']

            _category = ProductCategory.objects.filter(
                name=category_name).first()
            product['category'] = _category
            # Product.objects.create(**product)
            products_obj.append(Product(**product))
        Product.objects.bulk_create(products_obj)