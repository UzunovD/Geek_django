import json
import os

from authapp.models import ShopUser, ShopUserProfile
from django.conf import settings
from django.core.management.base import BaseCommand


def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, f'{file_name}.json'),
              encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'add DB new data. If user have bo profile'

    def handle(self, *args, **options):
        users_to_update = ShopUser.objects.filter(shopuserprofile__isnull=True)
        print(users_to_update.count())

        for user in users_to_update:
            ShopUserProfile.objects.create(user=user)

