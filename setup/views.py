from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Brand
from .forms import BrandForm
# Create your views here.

def all_brands(request):
    """ A view to show all brands """

    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    return render(request, 'setup/brands.html', context)


def brand_detail(request, brand_id):
    """ A view to show brand detail """
    brand = get_object_or_404(Brand, pk=brand_id)

    context = {
        'brand': brand,
    }

    return render(request, 'setup/brand_detail.html', context)


@login_required
def add_brand(request):
    """ Add a brand to the setup """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.save()
            messages.success(request, 'Successfully added brand!')
            return redirect(reverse('brand_detail', args=[brand.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = BrandForm()

    template = 'setup/add_brand.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_brand(request, brand_id):
    """ View to edit brand """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated brand!')
            return redirect(reverse('brand_detail', args=[brand.id]))
        else:
            messages.error(request, 'Failed to update brand. Please ensure the form is valid.')
    else:
        form = BrandForm(instance=brand)
        messages.info(request, f'You are editing {brand.name}')

    template = 'setup/edit_brand.html'
    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, template, context)


@login_required
def delete_brand(request, brand_id):
    """ Delete a brand from the setup """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    brand.delete()
    messages.success(request, 'brand deleted!')
    return redirect(reverse('brands'))
