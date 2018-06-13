from django.contrib import admin
from .models import Product, Image


class ImageAdmin(admin.StackedInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "details", "about_brand", "sizing", "shipping"]
    inlines = [ImageAdmin]


admin.site.register(Product, ProductAdmin)