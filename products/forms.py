from django import forms
from .widgets import CustomClearableFileInput
from .models import Product
from setup.models import Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    promo_side_banner_left = forms.ImageField(label='Promo Side Banner Left', required=False, widget=CustomClearableFileInput)

    promo_side_banner_right = forms.ImageField(label='Promo Side Banner Right', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
