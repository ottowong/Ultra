from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from .models import Product, Type

def index(request):
    productList = Product.objects.order_by("-pk")[:12]
    typeList = Type.objects.order_by("-pk")
    product2List = []
    for i in range(0,len(productList)):
        product2List.append([Type.objects.get(pk = productList[i].typeId.pk), productList])
    template = loader.get_template('main/index.html')
    context = {
        'product2List': product2List,
        'typeList' : typeList,
    }
    return HttpResponse(template.render(context, request))

def product(request, productId):
    template = loader.get_template('main/product.html')
    productList = Product.objects.order_by("-pk")[:12]
    typeList = Type.objects.order_by("-pk")
    product2List = []
    for i in range(0,len(productList)):
        product2List.append([Type.objects.get(pk = productList[i].typeId.pk), productList])
    context = {
        'product2List': product2List,
        'typeList' : typeList,
    }
    return HttpResponse(template.render(context,request))

def bob(request):
    template = loader.get_template('main/bob.html')
    context={}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("main/login.html")
    context = {}
    return HttpResponse(template.render(context,request))

def cart(request):
    template = loader.get_template("main/cart.html")
    context = {}
    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template("main/contact.html")
    context = {}
    return HttpResponse(template.render(context,request))

def shipping(request):
    template = loader.get_template("main/shipping.html")
    context = {}
    return HttpResponse(template.render(context,request))

def social(request):
    template = loader.get_template("main/social.html")
    context = {}
    return HttpResponse(template.render(context,request))
