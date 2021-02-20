from django import forms
from products.widgets import CustomClearableFileInput
from .models import Brand, KeyFeatures, Feature, Specification, Spec, Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    image = forms.ImageField(label='Category Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'

    brand_logo = forms.ImageField(label='Brand Logo', required=False, widget=CustomClearableFileInput)

    side_banner = forms.ImageField(label='Side Banner', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in brands]


class KeyFeaturesForm(forms.ModelForm):

    class Meta:
        model = KeyFeatures
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        keyfeatures = KeyFeatures.objects.all()


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        feature = Feature.objects.all()


class SpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        specification = Specification.objects.all()


class SpecForm(forms.ModelForm):

    class Meta:
        model = Spec
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        spec = Spec.objects.all()

