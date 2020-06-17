from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def product(request):
    return render(request, 'mainapp/product.html')

def product_deails(request):
    return render(request, 'mainapp/product-deails.html')
