from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/<int:productId>', views.product, name="product"),
    path('bob', views.bob, name="bob"),
]
