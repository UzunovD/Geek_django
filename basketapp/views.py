from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from mainapp.models import Product
from basketapp.models import Basket


def add_product(request, pk_prod):
    basket = request.user.basket.filter(product=pk_prod).first()

    if not basket:
        basket = Basket(user=request.user, product=get_object_or_404(Product, pk=pk_prod))

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

