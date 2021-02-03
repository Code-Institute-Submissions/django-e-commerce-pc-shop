from django.contrib import admin
from .models import (
  Brand, KeyFeatures, Feature, Specification, Spec, Category)

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)
    list_display = (
        'friendly_name',
        'name',
        'image_preview',
    )


class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ('logo_preview',)
    list_display = (
        'friendly_name',
        'name',
        'logo_preview',
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
admin.site.register(Category, CategoryAdmin)
