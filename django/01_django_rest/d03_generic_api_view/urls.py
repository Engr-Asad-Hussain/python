from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.ReviewsListCreateAPIView.as_view()),
    path("reviews/<int:pk>/", views.ReviewListUpdateDeleteApiView.as_view()),
]
