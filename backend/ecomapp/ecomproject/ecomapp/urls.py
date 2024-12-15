from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.getAllProducts, name="all-products"),
    path('api/products/<int:pk>/', views.getProduct, name="get-product"),  # For getting a single product by ID
    path('api/products/add/', views.addProduct, name="add-product"),      # For adding a product
    path('api/products/search/<str:keyword>/', views.searchProduct, name="search-products"),  # For searching products
]