from django.urls import path
from . import views

urlpatterns = [
    path("sellers/", views.Sellers.as_view()),
    path("sellers/<int:pk>/", views.SellerDetail.as_view()),
]
