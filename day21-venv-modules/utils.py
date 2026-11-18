def format_price(amount):
    return f"{amount} грн"
def cart_total(products):
    return sum(product.total() for product in products)
if __name__ == "__main__":
    print("Testing utils:", format_price(100))