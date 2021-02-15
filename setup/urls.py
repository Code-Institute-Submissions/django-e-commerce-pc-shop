from django.urls import path

from . import views

urlpatterns = [
    path('brands/', views.all_brands, name='brands'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('brands/add/', views.add_brand, name='add_brand'),
    path('brands/edit/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('brands/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('keyfeatures/', views.all_keyfeatures, name='keyfeatures'),
    path('keyfeatures/<int:keyfeatures_id>/', views.keyfeatures_detail, name='keyfeatures_detail'),
    path('keyfeatures/add/', views.add_keyfeatures, name='add_keyfeatures'),
    path('keyfeatures/edit/<int:keyfeatures_id>/', views.edit_keyfeatures, name='edit_keyfeatures'),
    path('keyfeatures/delete/<int:keyfeatures_id>/', views.delete_keyfeatures, name='delete_keyfeatures'),
    path('features/', views.all_features, name='features'),
    path('feature/add', views.add_feature, name='add_feature'),
    path('feature/delete/<int:feature_id>/', views.delete_feature, name='delete_feature'),
]
