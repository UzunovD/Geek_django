from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def index(request):
    products4 = Product.objects.all()[:4]
    products6 = Product.objects.all()[4:10]
    context = {
        'page_title': 'shop',
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
        'page_title': 'contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    context = {
        'page_title': 'products',
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context)


def product_details(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    products3 = Product.objects.all()[4:7]

    context = {
        'page_title': 'product deails',
        'categories': categories,
        'products': products,
        'products3': products3,
    }
    return render(request, 'mainapp/product_details.html', context)
