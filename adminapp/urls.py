from django.urls import path, re_path

from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/', adminapp.my_admin_users, name='users'),
    path('user/create/', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    re_path(r'^user/recover/(?P<pk>\d+)/$', adminapp.user_recover, name='user_recover'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
]


