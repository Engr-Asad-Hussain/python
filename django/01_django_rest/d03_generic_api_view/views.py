"""
- Concrete-View-Class: https://www.django-rest-framework.org/api-guide/generic-views/#listmodelmixin
"""

from rest_framework import generics

from .models import Reviews
from .serializers import ReviewsSerializers


# Depreciated
class ReviewsListApiView(generics.ListAPIView):
    """
    - Method: GET
    - Used for read-only endpoints to represent a collection of model instances.
    - Provides a `get` method handler.
    Notes:
    - ListAPIView extends from GenericAPIView, ListModelMixin
    - GenericAPIView extends from APIView class
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers


# Depreciated
class ReviewsCreateApiView(generics.CreateAPIView):
    """
    - Method: POST
    - Used for create-only endpoints.
    - Provides a `post` method handler.
    Notes:
    - CreateAPIView extends from GenericAPIView, CreateModelMixin
    - GenericAPIView extends from APIView class
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers


class ReviewsListCreateAPIView(generics.ListCreateAPIView):
    """
    - Method: GET, POST
    - Used for read-write endpoints to represent a collection of model instances.
    - Provides get and post method handlers.
    Notes:
    - ListCreateAPIView extends from GenericAPIView, ListModelMixin, CreateModelMixin
    - GenericAPIView extends from APIView class
    - Since, ReviewsCreateApiView, ReviewsListApiView have same definition we can combine
    them into single class.
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

    def perform_create(self, serializer):
        """
        - This method is provided by the mixin classes, and provide easy overriding of the object
        save or deletion behavior.
        Notes:
        - These hooks are particularly useful for setting attributes that are implicit in the
        request, but are not part of the request data.
        - These override points are also particularly useful for adding behavior that occurs
        before or after saving an object, such as emailing a confirmation, or logging the update.
        """

        return super().perform_create(serializer)


# Depreciated
class ReviewRetrieveApiView(generics.RetrieveAPIView):
    """
    - Method: GET
    - Used for read-only endpoints to represent a single model instance.
    - Provides a `get` method handler.\n
    Notes:
    - RetrieveAPIView extends from GenericAPIView, RetrieveModelMixin
    - GenericAPIView extends from APIView class
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = "pk"


# Depreciated
class ReviewUpdateApiView(generics.UpdateAPIView):
    """
    - Method: PUT/PATCH
    - Used for update-only endpoints for a single model instance.
    - Provides put and patch method handlers.
    Notes:
    - UpdateAPIView extends GenericAPIView, UpdateModelMixin
    - GenericAPIView extends from APIView class
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = "pk"


# Depreciated
class ReviewDeleteApiView(generics.DestroyAPIView):
    """
    - Method: DELETE
    - Used for delete-only endpoints for a single model instance.
    - Provides a delete method handler.
    Note:
    - DestroyAPIView extends GenericAPIView, DestroyModelMixin
    - GenericAPIView extends from APIView class
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = "pk"


class ReviewListUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    - Used for read-write-delete endpoints to represent a single model instance.
    - Provides get, put, patch and delete method handlers.
    Notes:
    - RetrieveUpdateDestroyAPIView extends GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
    - GenericAPIView extends from APIView class
    - Since, ReviewRetrieveApiView, ReviewUpdateApiView, ReviewDeleteApiView have same
    definition we can combine them into single class.
    """

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = "pk"

    def perform_update(self, serializer):
        """
        - This method is provided by the mixin classes, and provide easy overriding of the object
        save or deletion behavior.
        Notes:
        - These hooks are particularly useful for setting attributes that are implicit in the
        request, but are not part of the request data.
        - These override points are also particularly useful for adding behavior that occurs
        before or after saving an object, such as emailing a confirmation, or logging the update.
        """
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        """
        - This method is provided by the mixin classes, and provide easy overriding of the object
        save or deletion behavior.
        Notes:
        - These hooks are particularly useful for setting attributes that are implicit in the
        request, but are not part of the request data.
        - These override points are also particularly useful for adding behavior that occurs
        before or after saving an object, such as emailing a confirmation, or logging the update.
        """

        return super().perform_destroy(instance)
