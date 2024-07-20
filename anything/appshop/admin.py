from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    pass

class ReviewsAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Reviews, ReviewsAdmin)

