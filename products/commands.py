from dataclasses import dataclass
from decimal import Decimal
from .models import Product


@dataclass
class CreateProductCommand:
    name: str
    description: str
    price: Decimal
    stock: int


@dataclass
class UpdateProductCommand:
    id: int
    name: str = None
    description: str = None
    price: Decimal = None
    stock: int = None


class ProductCommandHandler:
    @staticmethod
    def handle_create_product(command: CreateProductCommand) -> Product:
        product = Product.objects.create(
            name=command.name,
            description=command.description,
            price=command.price,
            stock=command.stock,
        )
        return product

    @staticmethod
    def handle_update_product(command: UpdateProductCommand) -> Product:
        product = Product.objects.get(id=command.id)

        if command.name is not None:
            product.name = command.name
        if command.description is not None:
            product.description = command.description
        if command.price is not None:
            product.price = command.price
        if command.stock is not None:
            product.stock = command.stock

        product.save()
        return product
