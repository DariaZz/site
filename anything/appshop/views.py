from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Internet site</h1>Привет! Тут скоро будет магазин <img src= 'https://avatars.mds.yandex.net/i?id=be3988e409cba5545c83ff3b066888914f11f171-12472657-images-thumbs&n=13' >")
