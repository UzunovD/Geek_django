from django.urls import path, re_path

from my_ordersapp import views as my_ordersapp

app_name = 'my_ordersapp'

urlpatterns = [
    path('', my_ordersapp.OrdersList.as_view(), name='view'),
    path('create/', my_ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', my_ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', my_ordersapp.OrderItemsDelete.as_view(), name='order_delete'),
]
