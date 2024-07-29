
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Reviews


# Create your views here.
def hello(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        'products': products
    })


def view_product(request,id):
    product = Product.objects.filter(id=id).first()

    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        reviews = Reviews(author=author,text=text,product=product)
        reviews.save()

    reviews = product.reviews_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews
    })

def pay(request,id):
    return render(request, 'pay.html')
