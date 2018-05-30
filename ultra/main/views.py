from django.shortcuts import render, get_object_or_404
# Create your views here.

from .models import Product, Type, ProductImage, ProductColour, Colour

from django.http import HttpResponse

import math

def index(request):
    print(Product.objects.get(pk = 3))
    productList = Product.objects.order_by("-pk")[:12]
    typeList = Type.objects.order_by("-pk")
    product2List = []
    for i in range(0,len(productList)):
        product2List.append([Type.objects.get(pk = productList[i].typeId.pk), productList[i]])

    context = {
        'product2List': product2List,
        'typeList' : typeList,
    }
    return render(request, "main/index.html", context)

def product(request, productId):
    product = get_object_or_404(Product, pk=productId)
    images = ProductImage.objects.filter(productId = productId)
    imageList = []
    imageList.append(product.image)
    for i in range(0, images.count()):
        imageList.append(images[i].image)

    imageList = imageList[::-1]

    imageSet = [[] * 4 for i in range(int(math.ceil( len(imageList) / 4 )))]
    for i in range(0, math.ceil((len(imageList))/4)):
        if (len(imageList) >= 3):
            loops = 4
        else:
            loops = (len(imageList) % 4)
        for j in range(0,loops):
            newImage = imageList.pop()
            imageSet[i].append(newImage)


    productColours = ProductColour.objects.filter(productId = productId)

    colours = []
    for i in range(0, len(productColours)):
        colours.append(productColours[i].colourId)




    context = {
        'product': product,
        'imageSet': imageSet,
        'colours': colours,
    }
    return render(request, "main/product.html", context)

def addtobasket(request, productId):
    size = request.POST.get('size', 'medium')
    colour = int(request.POST.get('colour', 'black'))
    if "basket" in request.session:
        request.session["basket"] += [[productId,size,colour]]
    else:
        request.session["basket"] = [[productId,size,colour]]

    print(request.session["basket"])

    context = {
        'size': size,
        'colour': colour,
    }
    return render(request, "main/addtobasket.html", context)

def bob(request):
    context={}
    return render(request, "main/bob.html", context)

def login(request):
    context = {}
    return render(request, "main/login.html", context)

def basket(request):
    basket = request.session["basket"]
    print(basket)
    context = {
        'basket': basket
    }
    return render(request, "main/basket.html", context)

def contact(request):
    context = {}
    return render(request, "main/contact.html", context)

def shipping(request):
    context = {}
    return render(request, "main/shipping.html", context)

def social(request):
    context = {}
    return render(request, "main/social.html", context)

def register(request):
    context = {}
    if request.method == "POST":
        template = "main/register.html"
        form = ContactForm(request.POST)
        print("FORM")
        print(form.cleaned_data)
        if form.is_valid():
            print("NICE")
            print(form.cleaned_data)
            context = {
                'form' : form
            }
    else:
        template = "main/login.html"
    return render(request, template, context)

def logmein(request):
    template = loader.get_template("main/logmein.html")
    context = {}
    return HttpResponse(template.render(context,request))
