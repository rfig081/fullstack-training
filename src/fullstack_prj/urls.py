"""fullstack_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

# from first_app import views
# from forms_app import views
# from templates_app import views
# from auth_app import views
from cbv_app import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('admin/', admin.site.urls),
    
    # path('first_app/', include('first_app.urls')),
    # path('formpage/', views.form_name_view, name='form_name'),
    # path('templates_app/', include('templates_app.urls')),
    # path('auth_app/', include('auth_app.urls')),
    # path('logout/', views.user_logout, name='logout'),
    # path('special/', views.special, name='special'),
    path('cbv_app/', include('cbv_app.urls'), name='cbv_app'),
]
