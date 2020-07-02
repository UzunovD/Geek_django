from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product

def get_basket(request):
    return request.user.is_authenticated and request.user.basket.all() or []



def index(request):
    products4 = Product.objects.all()[:4]
    products6 = Product.objects.all()[4:10]
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
    categories = ProductCategory.objects.all()
    if pk == '0':
        products = Product.objects.all()
        category ={'name': 'all'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

    context = {
        'page_title': 'products',
        'categories': categories,
        'products': products,
        'basket': get_basket(request),
        'category': category,
    }
    return render(request, 'mainapp/products.html', context)


def product_details(request):
    categories = ProductCategory.objects.all()
    products3 = Product.objects.all()[4:7]

    context = {
        'page_title': 'product deails',
        'categories': categories,
        'basket': get_basket(request),
        'products3': products3,
    }
    return render(request, 'mainapp/product_details.html', context)
