from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)
    list_display = (
        'name',
        'image_preview',
    )


admin.site.register(Product, ProductAdmin)
