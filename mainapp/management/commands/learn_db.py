
from django.core.management import BaseCommand
from django.db import connection
from django.db.models import Q

from mainapp.models import Product
from geekshop.utils import db_profile_by_type


class Command(BaseCommand):
    def handle(self, *args, **options):
        some_test_products = Product.objects.select_related().filter(
            Q(category__name='modern')|
            Q(type_prod='lamp')
        )
        print(some_test_products)

        db_profile_by_type('lern_db', '', connection.queries)
