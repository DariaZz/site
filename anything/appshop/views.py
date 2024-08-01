import telebot
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .models import Reviews


from .config. import API_TOKEN, CHAT_ID

bot = telebot.TeleBot(API_TOKEN)

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
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('fullname')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        print(name, adress, phone)
        bot.send_message(CHAT_ID, f'''💸 Заказ: {product.name} ({product.price} рублей)

ФИО заказчика: {name}
Адрес доставки: {address}
Телефон: {phone}''')
        return redirect('/success')

    return render(request, 'pay.html', {
        'product': product
    })
def pay_successful(request):
    return render(request, 'successful.html')
