from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/<int:productId>', views.product, name="product"),
    path('bob', views.bob, name="bob"),
    path('login', views.login, name="login"),
    path('cart', views.cart, name="cart"),
    path('contact', views.contact, name="contact"),
    path('shipping', views.shipping, name="shipping"),
    path('social', views.social, name="social"),
    path('register', views.register, name="register"),
    path('logmein', views.logmein, name="logmein"),
]
