from django.urls import path, re_path

from my_ordersapp import views as my_ordersapp

app_name = 'my_ordersapp'

urlpatterns = [
    path('', my_ordersapp.OrdersList.as_view(), name='view'),
    path('create/', my_ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', my_ordersapp.OrderDetail.as_view(), name='order_detail'),
    path('update/<int:pk>/', my_ordersapp.OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', my_ordersapp.OrderDelete.as_view(), name='order_delete'),
    path('confirm/<int:pk>/', my_ordersapp.order_confirm, name='order_confirm'),
]
