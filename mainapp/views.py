import random

from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product


def get_menu():
    return ProductCategory.objects.filter(is_active=True)


def get_basket(request):
    return request.user.is_authenticated and request.user.basket.all() or []


def index(request):
    products4 = Product.objects.filter(is_active=True)[:4]
    products6 = Product.objects.filter(is_active=True)[4:10]
    context = {
        'page_title': 'shop',
        'basket': get_basket(request),
        'products4': products4,
        'products6': products6,
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
        'basket': get_basket(request),
        'page_title': 'contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request, pk):
    if pk == '0':
        products = Product.objects.filter(is_active=True)
        category = {'name': 'all'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.filter(is_active=True)

    context = {
        'page_title': 'products',
        'categories': get_menu(),
        'products': products,
        'basket': get_basket(request),
        'category': category,
    }
    return render(request, 'mainapp/products.html', context)


def product_page(request, pk_prod):
    product = get_object_or_404(Product, pk=pk_prod)
    # related_products = product.category.product_set.filter(type_prod = product.type_prod).exclude(pk=pk_prod)
    context = {
        'categories': get_menu(),
        'category': product.category,
        'page_title': 'product details',
        'basket': get_basket(request),
        # 'related_products': related_products[:3],
        'product': product,
    }
    return render(request, 'mainapp/product_page.html',context)


def product_details(request):
    hot_deal_pk = random.choice(Product.objects.filter(is_active=True).values_list('pk', flat=True))
    hot_deal = Product.objects.get(pk=hot_deal_pk)
    related_products = hot_deal.category.product_set.filter(is_active=True).filter(type_prod = hot_deal.type_prod).exclude(pk=hot_deal_pk)

    context = {
        'page_title': 'product details',
        'categories': get_menu(),
        'basket': get_basket(request),
        'related_products': related_products[:3],
        'hot_deal': hot_deal,
    }
    return render(request, 'mainapp/product_details.html', context)
