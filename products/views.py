from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def guitars(request):
    products = Product.objects.filter(category='guitars')
    return render(request, "guitars.html", {"products": products})

def keyboards(request):
    products = Product.objects.filter(category='keyboards')
    return render(request, "keyboards.html", {"products": products})  

def percussion(request):
    products = Product.objects.filter(category='percussion')
    return render(request, "percussion.html", {"products": products})      

def product_detail(request, pk):
    products = Product.objects.filter(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    
    return render(request, "product_detail.html", {'product': product,
                  'products': products})

def guitar_detail(request, pk):
    products = Product.objects.filter(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    
    return render(request, "guitar_detail.html", {'product': product,
                  'products': products})