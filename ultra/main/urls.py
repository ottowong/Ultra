from django.urls import path
import os

import django

from . import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'products/<int:productId>', views.product, name="product"),
    path(r'products/<int:productId>/addtobasket', views.addtobasket, name="product"),
    path(r'bob', views.bob, name="bob"),
    path(r'login', views.login, name="login"),
    path(r'basket', views.basket, name="basket"),
    path(r'contact', views.contact, name="contact"),
    path(r'shipping', views.shipping, name="shipping"),
    path(r'social', views.social, name="social"),
    path(r'register', views.register, name="register"),
    path(r'logmein', views.logmein, name="logmein"),
]