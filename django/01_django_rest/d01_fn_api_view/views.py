"""
- Function-Based-Views: https://www.django-rest-framework.org/api-guide/views/#api_view
"""

from rest_framework import decorators
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Products
from .serializers import ProductsSerializer


@decorators.api_view(["GET", "POST"])
def products(request: Request) -> Response:
    method = request.method
    if method == "GET":
        # List all the products from database
        queryset = Products.objects.all()

        # Serialize all the products (many=True)
        serializer = ProductsSerializer(queryset, many=True)

        # Return the serialized response
        return Response(serializer.data)

    if method == "POST":
        # Validate the request-body with Serializer
        serializer = ProductsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Save the request-body in database
        serializer.save()

        # Return the serialized response
        return Response(serializer.data)


@decorators.api_view(["GET", "PUT", "DELETE"])
def product_detail(request: Request, pk: int) -> Response:
    method = request.method
    try:
        # Fetch the product object with Primary-Key
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response({"message": "Product does not exists."})

    if method == "GET":
        # Serialize the single product object (many=False)
        serializer = ProductsSerializer(product, many=False)

        # Return the serialized response
        return Response(serializer.data)

    if method == "PUT":
        # Validate the request-body with Serializer & Product instance
        serializer = ProductsSerializer(product, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Save the request-body in database
        serializer.save()

        # Return the serialized response
        return Response(serializer.data)

    if method == "DELETE":
        # Delete the product object from the database
        product.delete()

        # Return the serialized response
        return Response({"message": "Product has been deleted."})
