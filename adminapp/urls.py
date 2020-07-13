from django.urls import path, re_path

from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('', adminapp.my_admin_users, name='users'),
    path('', adminapp.ShopUserList.as_view(), name='users'),
    # path('user/create/', adminapp.user_create, name='user_create'),
    path('user/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    re_path(r'user/recover/(?P<pk>\d+)/$', adminapp.user_recover, name='user_recover'),

    # path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(),
         name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    # path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(),
         name='category_update'),
    # path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(),
         name='category_delete'),

    path('category/<int:pk>/products', adminapp.category_products, name='category_products'),

    path('category/<int:pk>/product/create/', adminapp.product_create, name='product_create'),
    # path('product/<int:pk>/read/', adminapp.product_read, name='product_read'),
    path('product/<int:pk>/read/', adminapp.ProductDetailView.as_view(),
         name='product_read'),
    path('product/<int:pk>/update/', adminapp.product_update, name='product_update'),
    path('product/<int:pk>/delete/', adminapp.product_delete, name='product_delete'),

]


