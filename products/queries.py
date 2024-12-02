from django.db.models import Q
from .models import Product


class ProductQueryHandler:
    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return Product.objects.get(id=product_id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def search_products(search_term: str):
        return Product.objects.filter(
            Q(name__icontains=search_term) | Q(description__icontains=search_term)
        )

    @staticmethod
    def get_products_in_stock():
        return Product.objects.filter(stock__gt=0)
