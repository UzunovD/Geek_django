from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='age', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
