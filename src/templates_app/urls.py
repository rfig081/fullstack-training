from django.urls import path, re_path
from django.conf.urls import include
from . import views

#TEMPLATE TAGGING
app_name = 'templates_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
