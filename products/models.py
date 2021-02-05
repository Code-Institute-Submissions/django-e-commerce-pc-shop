from django.db import models

from django.utils.safestring import mark_safe

# Create your models here.


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=254, blank=False)
    available = models.BooleanField(default=True, null=True, blank=False)
    category = models.ForeignKey(
        'setup.Category', related_name="categories",
        null=True, blank=False, on_delete=models.SET_NULL)
    brand = models.ForeignKey(
        'setup.Brand', related_name="brands",
        null=True, blank=False, on_delete=models.SET_NULL)
    key_feature = models.ForeignKey(
        'setup.KeyFeatures', related_name="key_features",
        null=True, blank=False, on_delete=models.SET_NULL)
    chipset_logo = models.ForeignKey(
        'setup.Brand', related_name='chipset_logos',
        null=True, blank=True, on_delete=models.SET_NULL)
    additional_logo = models.ForeignKey(
        'setup.Brand', related_name='additional_logos',
        null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=False)
    specification = models.ForeignKey(
        'setup.Specification', related_name='Specs',
        null=True, blank=False, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    promo_side_banner_left = models.ImageField(null=True, blank=True)
    promo_side_banner_right = models.ImageField(null=True, blank=True)
    promo_side_banner_bottom = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="120" height="80" />'.format(self.image.url))
        else:
            return '(No image)'

    def __str__(self):
        return self.name
