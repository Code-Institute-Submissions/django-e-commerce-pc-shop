from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Brand, KeyFeatures, Feature, Specification, Spec
from .forms import (
    BrandForm, KeyFeaturesForm, FeatureForm, SpecificationForm, SpecForm)


# Create your views here.


def all_brands(request):
    """ A view to show all brands """

    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    return render(request, 'setup/brands.html', context)


def brand_detail(request, brand_id):
    """ A view to show brand details """

    brand = get_object_or_404(Brand, pk=brand_id)

    context = {
        'brand': brand,
    }

    return render(request, 'setup/brand_detail.html', context)


@login_required
def add_brand(request):
    """ Add a brand to the brands """

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
            messages.error(request,'Failed to add brand. Please ensure the form is valid.')
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
            messages.error(request,'Failed to update brand. Please ensure the form is valid.')
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
    """ Delete a brand from the brands """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    brand.delete()
    messages.success(request, 'Brand deleted!')
    return redirect(reverse('brands'))


def all_keyfeatures(request):
    """ A view to show all keyfeatures """

    keyfeatures = KeyFeatures.objects.all()

    context = {
        'keyfeatures': keyfeatures,
    }

    return render(request, 'keyfeatures/keyfeatures.html', context)


def keyfeatures_detail(request, keyfeatures_id):
    """ A view to show keyfeature detail """

    keyfeatures = get_object_or_404(KeyFeatures, pk=keyfeatures_id)

    context = {
        'keyfeatures': keyfeatures,
    }

    return render(request, 'keyfeatures/keyfeatures_detail.html', context)

@login_required
def add_keyfeatures(request):
    """ Add a keyfeature to the keyfeatures """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = KeyFeaturesForm(request.POST, request.FILES)
        if form.is_valid():
            keyfeatures = form.save()
            messages.success(request, 'Successfully added key features!')
            return redirect(reverse('keyfeatures'))
        else:
            messages.error(request, 'Failed to add key feature. Please ensure the form is valid.')
    else:
        form = KeyFeaturesForm()

    template = 'keyfeatures/add_keyfeatures.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_keyfeatures(request, keyfeatures_id):
    """ View to edit kefeatures """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    keyfeatures = get_object_or_404(KeyFeatures, pk=keyfeatures_id)
    if request.method == 'POST':
        form = KeyFeaturesForm(request.POST, request.FILES, instance=keyfeatures)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated key feature!')
            return redirect(reverse('keyfeatures_detail', args=[keyfeatures.id]))
        else:
            messages.error(request, 'Failed to update key feature. Please ensure the form is valid.')
    else:
        form = KeyFeaturesForm(instance=keyfeatures)
        messages.info(request, f'You are editing {keyfeatures.name}')

    template = 'keyfeatures/edit_keyfeatures.html'
    context = {
        'form': form,
        'keyfeatures': keyfeatures,
    }

    return render(request, template, context)


@login_required
def delete_keyfeatures(request, keyfeatures_id):
    """ Delete a brand from the brands """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    keyfeatures = get_object_or_404(KeyFeatures, pk=keyfeatures_id)
    keyfeatures.delete()
    messages.success(request, 'Keyfeature deleted!')
    return redirect(reverse('keyfeatures'))


def all_features(request):
    """ A view to show all features """

    features = Feature.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'features/features.html', context)


@login_required
def add_feature(request):
    """ Add a feature to the features """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():
            feature = form.save()
            messages.success(request, 'Successfully added feature!')
            return redirect(reverse('features'))
        else:
            messages.error(request, 'Failed to add feature. Please ensure the form is valid.')
    else:
        form = FeatureForm()

    template = 'features/add_feature.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_feature(request, feature_id):
    """ Delete a feature from the features """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    feature = get_object_or_404(Feature, pk=feature_id)
    feature.delete()
    messages.success(request, 'Feature deleted!')
    return redirect(reverse('features'))


def all_specifications(request):
    """ A view to show all specifications """

    specifications = Specification.objects.all()

    context = {
        'specifications': specifications,
    }

    return render(request, 'specifications/specifications.html', context)


def specification_detail(request, specification_id):
    """ A view to show specification detail """

    specification = get_object_or_404(Specification, pk=specification_id)

    context = {
        'specification': specification,
    }

    return render(request, 'specifications/specification_detail.html', context)


@login_required
def add_specification(request):
    """ Add a specification to the specifications """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SpecificationForm(request.POST, request.FILES)
        if form.is_valid():
            specification = form.save()
            messages.success(request, 'Successfully added specification!')
            return redirect(reverse('specifications'))
        else:
            messages.error(request, 'Failed to add key feature. Please ensure the form is valid.')
    else:
        form = SpecificationForm()

    template = 'specifications/add_specification.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_specification(request, specification_id):
    """ View to edit specification """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    specification = get_object_or_404(Specification, pk=specification_id)
    if request.method == 'POST':
        form = SpecificationForm(request.POST, request.FILES, instance=specification)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated specification!')
            return redirect(reverse('specification_detail', args=[specification.id]))
        else:
            messages.error(request, 'Failed to update key specification. Please ensure the form is valid.')
    else:
        form = SpecificationForm(instance=specification)
        messages.info(request, f'You are editing {specification.name}')

    template = 'specifications/edit_specification.html'
    context = {
        'form': form,
        'specification': specification,
    }

    return render(request, template, context)


@login_required
def delete_specification(request, specification_id):
    """ Delete a specification"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    specification = get_object_or_404(Specification, pk=specification_id)
    specification.delete()
    messages.success(request, 'Specification deleted!')
    return redirect(reverse('specifications'))


def all_specs(request):
    """ A view to show all features """

    specs = Spec.objects.all()

    context = {
        'specs': specs,
    }

    return render(request, 'specs/specs.html', context)


@login_required
def add_spec(request):
    """ Add a spec to the specs """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SpecForm(request.POST, request.FILES)
        if form.is_valid():
            spec = form.save()
            messages.success(request, 'Successfully added spec!')
            return redirect(reverse('specs'))
        else:
            messages.error(request, 'Failed to add spec. Please ensure the form is valid.')
    else:
        form = SpecForm()

    template = 'specs/add_spec.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_spec(request, spec_id):
    """ Delete a spec from the specs """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    spec = get_object_or_404(Spec, pk=spec_id)
    spec.delete()
    messages.success(request, 'Spec deleted!')
    return redirect(reverse('specs'))
