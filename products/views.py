from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal

from .models import Product
from .serializers import ProductSerializer
from .commands import CreateProductCommand, UpdateProductCommand, ProductCommandHandler
from .queries import ProductQueryHandler


class ProductViewSet(viewsets.ViewSet):
    # Query endpoints
    def list(self, request):
        products = ProductQueryHandler.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            product = ProductQueryHandler.get_product_by_id(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["get"])
    def search(self, request):
        search_term = request.query_params.get("q", "")
        products = ProductQueryHandler.search_products(search_term)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def in_stock(self, request):
        products = ProductQueryHandler.get_products_in_stock()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # Command endpoints
    def create(self, request):
        command = CreateProductCommand(
            name=request.data.get("name"),
            description=request.data.get("description"),
            price=Decimal(request.data.get("price")),
            stock=int(request.data.get("stock")),
        )
        product = ProductCommandHandler.handle_create_product(command)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        command = UpdateProductCommand(
            id=pk,
            name=request.data.get("name"),
            description=request.data.get("description"),
            price=Decimal(request.data.get("price"))
            if request.data.get("price")
            else None,
            stock=int(request.data.get("stock")) if request.data.get("stock") else None,
        )
        try:
            product = ProductCommandHandler.handle_update_product(command)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
