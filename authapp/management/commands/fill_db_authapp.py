import json
import os

from authapp.models import ShopUser
from django.conf import settings
from django.core.management.base import BaseCommand


def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, f'{file_name}.json'),
              encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        # users = load_from_json('users')
        #
        # ShopUser.objects.all().delete()
        # [ShopUser.objects.create(**user) for user in users]

        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser(username='django', email='', password='geekbrains')
