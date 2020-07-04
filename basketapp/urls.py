from django.urls import path, re_path

from basketapp import views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.view, name='view'),
    re_path(r'^add/product/(?P<pk_prod>\d+)$', basketapp.add_product, name='add_product'),
    re_path(r'^delete/product/(?P<pk_basket>\d+)/$', basketapp.delete_product, name='delete_product'),
    re_path(r'^change/(?P<pk_basket>\d+)/quantity/(?P<quantity>\d+)/$', basketapp.change_quantity, name='change_quantity'),
]


