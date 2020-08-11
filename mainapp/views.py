import random

from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from geekshop.settings import LOW_CACHE
from mainapp.models import ProductCategory, Product



def get_category(pk):
    if LOW_CACHE:
        key = f'productcategory_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True,
                                              category__is_active=True
                                              ).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True,
                                      category__is_active=True
                                      ).select_related('category')


def get_product(pk):
    if LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_in_category(pk):
    if LOW_CACHE:
        key = f'products_in_category_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True,
                                              category__is_active=True
                                              )
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True,
                                      category__is_active=True
                                      )



def index(request):
    products_ = get_products()
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
        products = get_products()
        category = {
            'name': 'all',
            'pk': pk,
        }
    else:
        category = get_category(pk)
        products = get_products_in_category(pk)

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
    product = get_product(pk_prod)
    context = {
        'category': product.category,
        'page_title': 'product details',
        'product': product,
    }
    return render(request, 'mainapp/product_page.html', context)


def product_details(request):
    hot_deal_pk = random.choice(
        Product.objects.filter(is_active=True, category__is_active=True
                               ).values_list('pk', flat=True))
    # hot_deal = Product.objects.get(pk=hot_deal_pk)
    hot_deal = get_product(hot_deal_pk)
    related_products = hot_deal.category.product_set.filter(is_active=True,
                                            category__is_active=True).filter(
        type_prod=hot_deal.type_prod).exclude(pk=hot_deal_pk)

    context = {
        'page_title': 'product details',
        'related_products': related_products[:3],
        'hot_deal': hot_deal,
    }
    return render(request, 'mainapp/product_details.html', context)


def product_details_async(request, pk):
    if request.is_ajax():
        try:
            # product = Product.objects.get(pk=pk)
            product = get_product(pk)
            return JsonResponse({
                'price': product.price,
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            })

