from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'shop',
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
    context = {
        'page_title': 'products',
    }
    return render(request, 'mainapp/products.html', context)


def product_details(request):
    context = {
        'page_title': 'product deails',
    }
    return render(request, 'mainapp/product_details.html', context)
