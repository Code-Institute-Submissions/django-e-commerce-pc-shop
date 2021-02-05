from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)
    list_display = (
        'name',
        'sku',
        'brand',
        'category',
        'available',
        'price',
        'rating',
        'image_preview',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
