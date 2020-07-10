from django.urls import path, re_path

from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('category/<int:pk>/products/', mainapp.products, name='products'),
    path('category/<int:pk>/products/<int:page>/', mainapp.products,
         name='products_pagination'),
    path('product/<int:pk_prod>/', mainapp.product_page, name='product_page'),
    path('product_details/', mainapp.product_details, name='product_details'),

]
