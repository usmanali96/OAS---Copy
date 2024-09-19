"""
URL configuration for oas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.aboutPage, name='about'),
    path('register/', views.register, name='register'),
    path('register-user/', views.registerUser, name='register-user'),
    path('login/', views.login, name='login'),
    path('contact/', views.contactPage, name='contact'),

 path('products/', views.product_list, name='product_list'),


    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/save_price/', views.save_price, name='save_price'),
    path('browse_product/', views.browse_page, name='browse_page'),
    path('add-product/', views.add_product_view, name='add_product'),
    path('shop/', views.shop_page, name='shop'),
    path('add-review/', views.add_review, name='add_review'),
    ]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
