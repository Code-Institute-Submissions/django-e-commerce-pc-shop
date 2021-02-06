from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product
from setup.models import Category
# Create your views here.


def all_products(request):
    """ A view to return show all products, including sorting and search
        And to return all categories names to use on dropdown menu
     """
    products = Product.objects.all()
    categories = Category.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,

        'categories': categories,
        'search_term': query,
    }

    print(products)
    print(categories)

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product detail """
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()

    context = {
        'product': product,
        'categories': categories,
    }

    print(product)

    return render(request, 'products/product_detail.html', context)
