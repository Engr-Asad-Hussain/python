from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products),
    path("products/<int:pk>/", views.product_detail),
]
