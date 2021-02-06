from django.shortcuts import render, get_object_or_404
from .models import Product
from setup.models import Category
# Create your views here.


def all_products(request):
    """ A view to return show all products, including sorting and search
        And to return all categories names to use on dropdown menu
     """
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    print(products)
    print(categories)

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product detail """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    print(product)

    return render(request, 'products/products_detail.html', context)
