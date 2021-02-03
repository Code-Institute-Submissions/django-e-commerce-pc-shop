
from django.db import models

from django.utils.safestring import mark_safe


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Category'

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="50" height="50" />'.format(self.image.url))
        else:
            return '(No image)'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(null=True, max_length=254, blank=False)
    brand_logo = models.ImageField(null=True, blank=True)
    side_banner = models.ImageField(null=True, blank=True)
    website = models.URLField(max_length=1024, null=True, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Brand'

    def logo_preview(self):
        if self.brand_logo:
            return mark_safe('<img src="{0}" width="50" height="50" />'.format(self.brand_logo.url))
        else:
            return '(No image)'

    def __str__(self):
        return self.friendly_name

    """ def get_friendly_name(self):
        return self.friendly_name """


class KeyFeatures(models.Model):

    class Meta:
        verbose_name_plural = 'Key Features'

    name = models.CharField(
      default='ProductCategory Features', max_length=254)

    feature_for = models.CharField(
      max_length=254, blank=True,
      default='Motherboard, Graphic Card etc. ')

    feature_1_name = models.ForeignKey(
      'Feature', related_name='feature_1_names', null=True,
      blank=True, on_delete=models.SET_NULL)

    feature_1 = models.CharField(
      max_length=254, blank=True)

    feature_2_name = models.ForeignKey(
      'Feature', related_name='feature_2_names', null=True,
      blank=True, on_delete=models.SET_NULL)

    feature_2 = models.CharField(
      max_length=254, blank=True)

    feature_3_name = models.ForeignKey(
      'Feature', related_name='feature_3_names', null=True,
      blank=True, on_delete=models.SET_NULL)

    feature_3 = models.CharField(
      max_length=254, blank=True)

    feature_4_name = models.ForeignKey(
      'Feature', related_name='feature_4_names', null=True,
      blank=True, on_delete=models.SET_NULL)

    feature_4 = models.CharField(
      max_length=254, blank=True)

    feature_5_name = models.ForeignKey(
      'Feature', default='test1', related_name='feature_5_names',
      null=True, blank=True, on_delete=models.SET_NULL)

    feature_5 = models.CharField(
      max_length=254, blank=True)

    def __str__(self):
        return self.feature_for

    """ def get_friendly_name(self):
        return self.name """


class Feature(models.Model):

    class Meta:
        verbose_name_plural = 'Feature'

    name = models.CharField(default='FeatureName', max_length=254)

    def __str__(self):
        return self.name


class Specification(models.Model):

    class Meta:
        verbose_name_plural = 'Specifications'

    name = models.CharField(
      default='of Specification!', max_length=254)

    specification_for = models.CharField(
      max_length=254, null=True, blank=False,
      default='Motherboard, Graphic Card, etc. ')

    spec_1_name = models.ForeignKey(
      'Spec', related_name='spec_1_names', null=True, blank=False,
      on_delete=models.SET_NULL)

    spec_1 = models.CharField(
      max_length=254, blank=False,
      default="Unfortunately we do not have any specification for this product.")

    spec_2_name = models.ForeignKey(
      'Spec', related_name='spec_2_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_2 = models.CharField(max_length=254, blank=True)

    spec_3_name = models.ForeignKey(
      'Spec', related_name='spec_3_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_3 = models.CharField(max_length=254, blank=True)

    spec_4_name = models.ForeignKey(
      'Spec', related_name='spec_4_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_4 = models.CharField(max_length=254, blank=True)

    spec_5_name = models.ForeignKey(
      'Spec', related_name='spec_5_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_5 = models.CharField(max_length=254, blank=True)

    spec_6_name = models.ForeignKey(
      'Spec', related_name='spec_6_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_6 = models.CharField(max_length=254, blank=True)

    spec_7_name = models.ForeignKey(
      'Spec', related_name='spec_7_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_7 = models.CharField(max_length=254, blank=True)

    spec_8_name = models.ForeignKey(
      'Spec', related_name='spec_8_names', null=True,
      blank=True, on_delete=models.SET_NULL)

    spec_8 = models.CharField(max_length=254, blank=True)

    spec_9_name = models.ForeignKey(
      'Spec', related_name='spec_9_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_9 = models.CharField(max_length=254, blank=True)

    spec_10_name = models.ForeignKey(
      'Spec', related_name='spec_10_names', null=True, blank=True,
      on_delete=models.SET_NULL)
    spec_10 = models.CharField(max_length=254, blank=True)

    spec_11_name = models.ForeignKey(
      'Spec', related_name='spec_11_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_11 = models.CharField(max_length=254, blank=True)

    spec_12_name = models.ForeignKey(
      'Spec', related_name='spec_12_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_12 = models.CharField(max_length=254, blank=True)

    spec_13_name = models.ForeignKey(
      'Spec', related_name='spec_13_names', null=True,
      blank=True, on_delete=models.SET_NULL)

    spec_13 = models.TextField(blank=True)

    spec_14_name = models.ForeignKey(
      'Spec', related_name='spec_14_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_14 = models.TextField(blank=True)

    spec_15_name = models.ForeignKey(
      'Spec', related_name='spec_15_names', null=True, blank=True,
      on_delete=models.SET_NULL)

    spec_15 = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Spec(models.Model):

    class Meta:
        verbose_name_plural = 'Spec'

    name = models.CharField(default='SpecName', max_length=254)

    def __str__(self):
        return self.name

