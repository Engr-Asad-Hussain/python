from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("categories", views.CategoriesApiView, basename="categories")
urlpatterns = router.urls
