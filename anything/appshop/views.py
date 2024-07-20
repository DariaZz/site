
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def hello(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        'products': products
    })

def view_product(request,id):
    product = Product.objects.filter(id=id).first()
    reviews = product.reviews_set.all()

    return render(request, 'product.html', {
        'product': product
    })
