"""
URL configuration for ecommerceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from ecommerceapp import views as ec
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ec.index),
    path('listitems/',ec.listitems,name='listitems'),
    path('listmoblie/',ec.listmoblie,name='listmoblie'),
    path('listcomputer/',ec.listcomputer,name='listcomputer'),
    path('listbook/',ec.listbook,name='listbook'),
    path('detials/<int:id>',ec.detials,name='detials'),
    path('add_to_cart/',ec.add_to_cart,name='add_to_cart'),
    path('checkout/',ec.checkout,name='checkout'),
    path('logout/', ec.auth_logout, name='logout'),
    path('auth_register/',ec.auth_register,name='auth_register'),
    path('auth_login/',ec.auth_login,name='auth_login'),
    path('payment/', ec.payment,name='payment'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
