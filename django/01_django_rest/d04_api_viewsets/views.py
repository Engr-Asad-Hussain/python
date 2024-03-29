"""
- ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
"""

from rest_framework import viewsets
from .models import Categories
from .serializers import CategoriesSerializer


class CategoriesApiView(viewsets.ModelViewSet):
    """
    - The ModelViewSet class inherits from GenericAPIView and includes implementations for various
    actions, by mixing in the behavior of the various mixin classes.
    - The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(),
    .update(), .partial_update(), and .destroy().
    """

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = "pk"
