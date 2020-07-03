from django.urls import path, re_path

from basketapp import views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.view, name='view'),
    re_path(r'^add/product/(?P<pk_prod>\d+)$', basketapp.add_product, name='add_product'),
]
