class Product:
    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def get_info(self):
        answer = f"Product ID: {self.product_id}\nName: {self.product_name}\nPrice: ${self.product_price}"
        return answer

class Book(Product):
    def __init__(self, product_id, product_name, product_price, book_author):
        super().__init__(product_id, product_name, product_price)
        self.book_author = book_author

    def get_info(self):
        answer = super().get_info() + f"\nAuthor: {self.book_author}\n---"
        return answer

class Electronics(Product):
    def __init__(self, product_id, product_name, product_price, manufacturer, warranty_period):
        super().__init__(product_id, product_name, product_price)
        self.manufacturer = manufacturer
        self.warranty_period = warranty_period

    def get_info(self):
        warranty_info = f"{self.warranty_period} years" if self.warranty_period else "NO WARRANTY"
        answer = super().get_info() + f"\nManufacturer: {self.manufacturer}\nWarranty Period: {warranty_info}\n---"
        return answer

class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        answer = sum(
            product.product_price for product in self.cart_items
            )
        return answer

    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        answer = total * (1 - discount_percentage / 100)
        return answer

    def display_cart(self):
        for product in self.cart_items:
            print(product.get_info())
        total_before_discount = self.calculate_total()
        print(f"Total price before discount: ${total_before_discount:.2f}")

def main():
    credit_cart = ShoppingCart()
    num_products = int(input())

    for _ in range(num_products):
        product_type = input().strip().lower()
        product_id = input().strip()
        product_name = input().strip()
        product_price = float(input().strip())

        if product_type == 'book':
            book_author = input().strip()
            credit_cart.add_product(Book(product_id, product_name, product_price, book_author))
        
        if product_type == 'electronics':
            manufacturer = input().strip()
            warranty_period = float(input().strip())
            credit_cart.add_product(Electronics(product_id, product_name, product_price, manufacturer, warranty_period))

    credit_cart.display_cart()
    total_after_discount = credit_cart.apply_discount(float(input()))
    print(f"Total price after discount: ${total_after_discount:.2f}")

if __name__ == "__main__":
    main()
