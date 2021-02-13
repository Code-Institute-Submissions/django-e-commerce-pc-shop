from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_brands, name='brands'),
    path('<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('add/', views.add_brand, name='add_brand'),
    path('edit/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
]
