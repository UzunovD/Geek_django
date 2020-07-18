from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from geekshop import settings


def get_activation_key_expires():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='age', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires

    def send_verify_email(self):
        verify_link = reverse(
            'auth:verify',
            kwargs={
                'email': self.email,
                'activation_key': self.activation_key,
            },
        )
        title = f'Account confirmation {self.username}'
        message = f'To confirm account {self.username} on the portal ' \
                  f'{settings.DOMAIN_NAME} click the link:' \
                  f' \n{settings.DOMAIN_NAME}{verify_link}'

        return send_mail(title,message,settings.EMAIL_HOST_USER,[self.email])
