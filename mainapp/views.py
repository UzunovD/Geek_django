from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'Shop',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'page_title': 'Contact',
    }
    return render(request, 'mainapp/contact.html', context)


def product(request):
    context = {
        'page_title': 'Product',
    }
    return render(request, 'mainapp/product.html', context)


def product_deails(request):
    context = {
        'page_title': 'Product deails',
    }
    return render(request, 'mainapp/product-deails.html', context)
