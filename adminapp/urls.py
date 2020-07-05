from django.urls import path, re_path

from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.my_admin_home, name='home'),
]


