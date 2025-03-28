class Product:
    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def get_info(self):
        return f"Product ID: {self.product_id}\nName: {self.product_name}\nPrice: ${self.product_price}"

class Book(Product):
    def __init__(self, product_id, product_name, product_price, book_author):
        super().__init__(product_id, product_name, product_price)
        self.book_author = book_author

    def get_info(self):
        return super().get_info() + f"\nAuthor: {self.book_author}\n---"

class Electronics(Product):
    def __init__(self, product_id, product_name, product_price, product_manufacturer, warranty_years):
        super().__init__(product_id, product_name, product_price)
        self.product_manufacturer = product_manufacturer
        self.warranty_years = warranty_years

    def get_info(self):
        warranty_info = f"{self.warranty_years} years" if self.warranty_years else "NO WARRANTY"
        return super().get_info() + f"\nManufacturer: {self.product_manufacturer}\nWarranty Period: {warranty_info}\n---"

class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def cal_all(self):
        return sum(product.product_price for product in self.cart_items)

    def apply_off(self, discount_percentage):
        total = self.cal_all()
        return total * (1 - discount_percentage / 100)

    def display_cart(self):
        for product in self.cart_items:
            print(product.get_info())
        total_before_discount = self.cal_all()
        print(f"Total price before discount: ${total_before_discount:.2f}")

def create_product(product_type, product_id, product_name, product_price,):
    if product_type == 'book':
        book_author = input().strip()
        return Book(product_id, product_name, product_price, book_author)
    elif product_type == 'electronics':
        product_manufacturer = input().strip()
        warranty_years = float(input().strip())

        return Electronics(product_id, product_name, product_price, product_manufacturer, warranty_years)
    else:
        raise ValueError("Unknown product type")

def main():
    quera = ShoppingCart()
    y = int(input())

    for _ in range(y):
        product_type = input().strip().lower()
        product_id = input().strip()
        product_name = input().strip()
        product_price = float(input().strip())
            
        product = create_product(product_type, product_id, product_name, product_price)
        quera.add_product(product)

    quera.display_cart()
    discount_percentage = float(input())
    total_after_discount = quera.apply_off(discount_percentage)
    print(f"Total price after discount: ${total_after_discount:.2f}")

if __name__ == "__main__":
    main()
