from django.urls import path

from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('products/', mainapp.products, name='products'),
    path('product_details/', mainapp.product_details, name='product_details'),

]
