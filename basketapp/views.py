from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from mainapp.models import Product
from basketapp.models import Basket


@login_required
def view(request):
    context = {
        'basket': request.user.basket.all(),
    }
    return render(request, 'basket/view.html', context)


@login_required
def delete_product(request, pk_basket):
    basket = get_object_or_404(Basket, pk=pk_basket)
    basket.delete()
    return HttpResponseRedirect(reverse('basket:view'))


@login_required
def add_product(request, pk_prod):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:product_page', args=[pk_prod]))

    basket = request.user.basket.filter(product=pk_prod).first()

    if not basket:
        basket = Basket(user=request.user, product=get_object_or_404(Product, pk=pk_prod))

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def change_quantity(request, pk_basket, quantity):
    quantity = int(quantity)
    if request.is_ajax():
        basket = request.user.basket.get(pk=int(pk_basket))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        basket = request.user.basket.all()
        context = {
            'basket': basket,
        }
        result = render_to_string('basket/includes/inc__basket_list.html', context)
        # print(result)
        return JsonResponse({'result': result})
