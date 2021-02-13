from django import forms
from products.widgets import CustomClearableFileInput
from .models import Brand


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

        """ self.fields['brands'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black' """
