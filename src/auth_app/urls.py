from django.urls import path, re_path
from django.conf.urls import include
from . import views

#TEMPLATE URLS
app_name = 'auth_app'

urlpatterns = [
    path('register/', views.register, name='register'),
]