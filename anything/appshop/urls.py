from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path ("product/<int:id>",views.view_product, name="view_product")
]