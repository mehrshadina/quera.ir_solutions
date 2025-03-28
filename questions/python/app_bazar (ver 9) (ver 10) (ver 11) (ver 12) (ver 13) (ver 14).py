class Product:
    def __init__(self, id_product, name_product, price):
        self.id_product = id_product
        self.name_product = name_product
        self.price = price

    def info(self):
        return f"Product ID: {self.id_product}\nName: {self.name_product}\nPrice: ${self.price}"

class Book(Product):
    def __init__(self, id_product, name_product, price, author):
        super().__init__(id_product, name_product, price)
        self.author = author

    def info(self):
        return super().info() + f"\nAuthor: {self.author}\n---"

class Electronics(Product):
    def __init__(self, id_product, name_product, price, manufacturer, warranty_period):
        super().__init__(id_product, name_product, price)
        self.manufacturer = manufacturer
        self.warranty_period = warranty_period

    def info(self):
        warranty = f"{self.warranty_period} years" if self.warranty_period else "NO WARRANTY"
        return super().info() + f"\nManufacturer: {self.manufacturer}\nWarranty Period: {warranty}\n---"

class ShoppingCart:
    def __init__(self):
        self.products = []

    def p_add(self, product):
        self.products.append(product)

    def calcul(self):
        return sum(product.price for product in self.products)

    def display(self):
        for product in self.products:
            print(product.info())
        before_discount = self.calcul()
        print(f"Total price before discount: ${before_discount:.2f}")

    def discount(self, discount_percentage):
        total = self.calcul()
        return total * (1 - discount_percentage / 100)


cart = ShoppingCart()
n = int(input())

for _ in range(n):
        type = input().strip().lower()

        if type == 'book':
            id_p = input().strip()
            name_p = input().strip()
            price = float(input().strip())
            author = input().strip()
            cart.p_add(Book(id_p, name_p, price, author))

        elif type == 'electronics':
            id_p = input().strip()
            name_p = input().strip()
            price = float(input().strip())
            manufacturer = input().strip()
            warranty_period = float(input().strip())
            cart.p_add(Electronics(id_p, name_p, price, manufacturer, warranty_period))

cart.display()
after_discount = cart.discount(float(input()))
print(f"Total price after discount: ${after_discount:.2f}")


