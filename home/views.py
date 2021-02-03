from django.shortcuts import render

from setup.models import Category

# Create your views here.


def index(request):
    """ A view to return the index page """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    print(categories)
    return render(request, 'home/index.html', context)
