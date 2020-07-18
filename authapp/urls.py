from django.urls import path

from authapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('register/', authapp.register, name='register'),
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('update/', authapp.update, name='update'),
    path('pass_change/', authapp.pass_change, name='pass_change'),
    path( 'verify/<str:email>/<str:activation_key>/', authapp.verify,
          name='verify'),
]
