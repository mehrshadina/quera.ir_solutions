class Product:
    def __init__(self, id_product, name_product, price):
        self.id_product = id_product
        self.name_product = name_product
        self.price = price

    def info_get(self):
        return f"Product ID: {self.id_product}\nName: {self.name_product}\nPrice: ${self.price}"

class Book(Product):
    def __init__(self, id_product, name_product, price, author):
        super().__init__(id_product, name_product, price)
        self.author = author

    def info_get(self):
        return super().info_get() + f"\nAuthor: {self.author}\n---"

class Electronics(Product):
    def __init__(self, id_product, name_product, price, manufacturer, warranty_period):
        super().__init__(id_product, name_product, price)
        self.manufacturer = manufacturer
        self.warranty_period = warranty_period

    def info_get(self):
        warranty = f"{self.warranty_period} years" if self.warranty_period else "NO WARRANTY"
        return super().info_get() + f"\nManufacturer: {self.manufacturer}\nWarranty Period: {warranty}\n---"

class ShoppingCart:
    def __init__(self):
        self.products = []

    def product_add(self, product):
        self.products.append(product)

    def total_calcul(self):
        return sum(product.price for product in self.products)

    def discount_apply(self, discount_percentage):
        total = self.total_calcul()
        return total * (1 - discount_percentage / 100)

    def display_cart(self):
        for product in self.products:
            print(product.info_get())
        total_before_discount = self.total_calcul()
        print(f"Total price before discount: ${total_before_discount:.2f}")

def main():
    cart = ShoppingCart()
    n = int(input())

    for _ in range(n):
        product_type = input().strip().lower()
        id_product = input().strip()
        name_product = input().strip()
        price = float(input().strip())

        if product_type == 'book':
            author = input().strip()
            cart.product_add(Book(id_product, name_product, price, author))
        elif product_type == 'electronics':
            manufacturer = input().strip()
            warranty_period = float(input().strip())
            cart.product_add(Electronics(id_product, name_product, price, manufacturer, warranty_period))

    cart.display_cart()
    discount_percentage = float(input())
    total_after_discount = cart.discount_apply(discount_percentage)
    print(f"Total price after discount: ${total_after_discount:.2f}")

if __name__ == "__main__":
    main()
