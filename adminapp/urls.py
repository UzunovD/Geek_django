from django.urls import path, re_path

from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.my_admin_home, name='home'),
    path('user/create/', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    re_path(r'^user/recover/(?P<pk>\d+)/$', adminapp.user_recover, name='user_recover'),
]


