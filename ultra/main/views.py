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
    print("TEST: ",product2List[0][1])
    print(typeList)
    return HttpResponse(template.render(context, request))

def product(request, productId):
    return HttpResponse("Product "+str(productId))

def bob(request):
    template = loader.get_template('main/bob.html')
    context={}
    return HttpResponse(template.render(context, request))
