from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int
    quantity: int = 1

    def total(self):
        return self.price * self.quantity