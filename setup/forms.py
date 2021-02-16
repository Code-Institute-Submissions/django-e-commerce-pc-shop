from django import forms
from products.widgets import CustomClearableFileInput
from .models import Brand, KeyFeatures, Feature


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

