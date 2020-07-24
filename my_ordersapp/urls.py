from django.urls import path, re_path

from my_ordersapp import views as my_ordersapp

app_name = 'my_ordersapp'

urlpatterns = [
    path('', my_ordersapp.OrdersView.as_view(), name='view'),
    # re_path(r'^add/product/(?P<pk_prod>\d+)/$', my_ordersapp.add_product, name='add_product'),
    # re_path(r'^delete/product/(?P<pk_my_orders>\d+)/$', my_ordersapp.delete_product, name='delete_product'),
    # re_path(r'^change/(?P<pk_my_orders>\d+)/quantity/(?P<quantity>\d+)/$', my_ordersapp.change_quantity),
]


