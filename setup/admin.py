from django.contrib import admin
from .models import (
  Brand, KeyFeatures, Feature, Specification, Spec)

from django.db.models.functions import Lower

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class MemoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class KeyFeaturesAdmin(admin.ModelAdmin):
    list_display = (
        'feature_for',
        'name',
        'feature_1_name',
        'feature_2_name',
        'feature_3_name',
        'feature_4_name',
        'feature_5_name',
    )


class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class SpecificationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class SpecAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Brand, BrandAdmin)
admin.site.register(KeyFeatures, KeyFeaturesAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(Spec, SpecAdmin)
