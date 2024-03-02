"""
- Class-Based-Views: https://www.django-rest-framework.org/api-guide/views/#class-based-views
"""

from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import SellerSerializer
from .models import Seller


class Sellers(views.APIView):
    def get(self, request: Request) -> Response:
        # List all the Sellers from database
        queryset = Seller.objects.all()

        # Serialize all the Sellers objects (many=True)
        serializer = SellerSerializer(queryset, many=True)

        # Return the serialized response
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        # Validate the request-body with Serializer
        serializer = SellerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Save the request-body in database
        serializer.save()

        # Return the serialized response
        return Response(serializer.data)

    def dispatch(self, request, *args, **kwargs):
        """
        - Dispatch method will be called before/after calling the view handler methods
        i.e., .get, .post.
        - This is an internal method used by django. You can perform certail actions before/after view.
        """

        view_result = super().dispatch(request, *args, **kwargs)
        return view_result

    def handle_exception(self, exc):
        """
        - Any exception thrown by the handler method will be passed to this method, which either returns a Response instance
        - If you need to customize the error responses your API returns you should subclass this method.
        """

        return super().handle_exception(exc)


class SellerDetail(views.APIView):
    def _get_seller(self, pk: int) -> Seller:
        try:
            # Fetch the Seller object with Primary-Key
            return Seller.objects.get(pk=pk)
        except Seller.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        seller = self._get_seller(pk)
        if seller is None:
            return Response({"message": "Seller does not exists."})

        # Serialize the single Seller object (many=False)
        serializer = SellerSerializer(seller, many=False)

        # Return the serialized response
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        seller = self._get_seller(pk)
        if seller is None:
            return Response({"message": "Seller does not exists."})

        # Validate the request-body with Serializer & Seller instance
        serializer = SellerSerializer(seller, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)

        # Save the request-body in database
        serializer.save()

        # Return the serialized response
        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        seller = self._get_seller(pk)
        if seller is None:
            return Response({"message": "Seller does not exists."})

        # Delete the Seller object from the database
        seller.delete()

        # Return the serialized response
        return Response({"message": "Seller has been deleted."})
