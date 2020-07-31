import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product


def index(request):
    products_ = Product.objects.filter(is_active=True, category__is_active=True)
    context = {
        'page_title': 'shop',
        'products4': products_[:4],
        'products6': products_[4:10],
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    locations = [
        {
            'loc': 'California',
            'phone': '1900 1234 5678 ',
            'email': 'info@interior.com',
            'address': '12 W 1st St, 90001 Los Angeles, California',
        },
        {
            'loc': 'Texas',
            'phone': '1900 1234 5678 ',
            'email': 'info@interior.com',
            'address': '12 W 1st St, 90001 New Jersia, Texas',
        },
        {
            'loc': 'Man',
            'phone': '1900 1234 5678 ',
            'email': 'info@interior.com',
            'address': '12 W 1st St, 90001 Saint Men, Man',
        },
    ]
    context = {
        'page_title': 'contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request, pk, page=1):
    if pk == 0:
        products = Product.objects.filter(is_active=True, category__is_active=True)
        category = {
            'name': 'all',
            'pk': pk,
        }
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.filter(is_active=True, category__is_active=True)

    if page != 0:
        products_paginator = Paginator(products, 3)
        try:
            products = products_paginator.page(page)
        except PageNotAnInteger:
            products = products_paginator.page(1)
        except EmptyPage:
            products = products_paginator.page(products_paginator.num_pages)


    context = {
        'page_title': 'products',
        'products': products,
        'category': category,
        'page': page,
    }
    return render(request, 'mainapp/products.html', context)


def product_page(request, pk_prod):
    product = get_object_or_404(Product, pk=pk_prod)
    context = {
        'category': product.category,
        'page_title': 'product details',
        'product': product,
    }
    return render(request, 'mainapp/product_page.html',context)


def product_details(request):
    hot_deal_pk = random.choice(Product.objects.filter(is_active=True,
                                                       category__is_active=True).values_list('pk', flat=True))
    hot_deal = Product.objects.get(pk=hot_deal_pk)
    related_products = hot_deal.category.product_set.filter(is_active=True,
                                                            category__is_active=True).filter(type_prod = hot_deal.type_prod).exclude(pk=hot_deal_pk)

    context = {
        'page_title': 'product details',
        'related_products': related_products[:3],
        'hot_deal': hot_deal,
    }
    return render(request, 'mainapp/product_details.html', context)


def product_details_async(request, pk):
    if request.is_ajax():
        try:
            produkt = Product.objects.get(pk=pk)
            return JsonResponse({
                'price': produkt.price,
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            })

