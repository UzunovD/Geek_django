from django.core.cache import cache

from geekshop.settings import LOW_CACHE
from mainapp.models import ProductCategory


def menu(request):
    if LOW_CACHE:
        key = 'catalog_menu'
        menu_ = cache.get(key)
        if menu_ is None:
            menu_ = ProductCategory.objects.filter(is_active=True)
            cache.set(key, menu_)
        return {
        'categories': menu_,
    }
    else:
        menu_ = ProductCategory.objects.filter(is_active=True)
    return {
        'categories': menu_,
    }