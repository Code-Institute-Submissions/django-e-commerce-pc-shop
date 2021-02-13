from django.urls import path

from . import views

urlpatterns = [
    path('brands/', views.all_brands, name='brands'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('brands/add/', views.add_brand, name='add_brand'),
    path('brands/edit/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('brands/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('keyfeatures/', views.all_keyfeatures, name='keyfeatures'),
    path('keyfeatures/add/', views.add_keyfeatures, name='add_keyfeatures'),
    path('feature/add', views.add_feature, name='add_feature'),
]
