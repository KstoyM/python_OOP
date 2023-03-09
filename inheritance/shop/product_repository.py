from shop.drink import Drink
from shop.food import Food
from shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> [Product, None]:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{p}: {p.quantity}" for p in self.products])


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)