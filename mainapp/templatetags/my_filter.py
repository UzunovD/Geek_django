from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='users_media_avatar')
def users_media_avatar(string):
    '''
    Auto add relative URL-path at media files users:
    /users_avatars/users1.png -> /media/users_avatars/users1.png
    adn set default img

    :param string:
    :return: string
    '''

    if not string:
        return '/media/users_avatars/default.png'

    return f'{settings.MEDIA_URL}{string}'
