from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from geekshop.settings import LOGIN_URL
from mainapp.models import Product
from geekshop.utils import db_profile_by_type


@login_required
def view(request):
    return render(request, 'basket/view.html')


@login_required
def delete_product(request, pk_basket):
    basket = get_object_or_404(Basket, pk=pk_basket)
    basket.delete()
    return HttpResponseRedirect(reverse('basket:view'))


@login_required
def add_product(request, pk_prod):
    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:product_page',
                                            kwargs={'pk_prod': pk_prod}))

    basket = request.user.basket.filter(product=pk_prod).first()

    if not basket:
        basket = Basket.objects.create(user=request.user,
                                        product=get_object_or_404(Product,
                                        pk=pk_prod), quantity=1)
    else:
        # basket.quantity += 1
        basket.quantity = F('quantity') + 1
        basket.save()
        db_profile_by_type(basket, 'UPDATE', connection.queries)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def change_quantity(request, pk_basket, quantity):
    quantity = int(quantity)
    if request.is_ajax():
        basket = get_object_or_404(Basket, pk=int(pk_basket))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        result = render_to_string('basket/includes/inc__basket_list.html',
                                  request=request)
        return JsonResponse({'result': result})

