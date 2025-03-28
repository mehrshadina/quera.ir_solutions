class Product:
    def __init__(self, id_product, name_product, price):
        self.id_product = id_product
        self.name_product = name_product
        self.price = float(price)

    def info_get(self):
        return f"Product ID: {self.id_product}\nName: {self.name_product}\nPrice: ${self.price:.2f}\n"


class Book(Product):
    def __init__(self, id_product, name_product, price, author):
        super().__init__(id_product, name_product, price)
        self.author = author

    def info_get(self):
        base_info = super().info_get()
        return f"{base_info}Author: {self.author}\n"


class Electronics(Product):
    def __init__(self, id_product, name_product, price, manufacturer, warranty_period):
        super().__init__(id_product, name_product, price)
        self.manufacturer = manufacturer
        self.warranty_period = float(warranty_period)

    def info_get(self):
        base_info = super().info_get()
        warranty_info = f"{self.warranty_period} years" if self.warranty_period > 0 else "NO WARRANTY"
        return f"{base_info}Manufacturer: {self.manufacturer}\nWarranty Period: {warranty_info}\n"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def product_add(self, product):
        self.products.append(product)

    def product_remove(self, product):
        self.products.remove(product)

    def total_calcul(self):
        return sum(product.price for product in self.products)

    def discount_apply(self, discount_percentage):
        total_price = self.total_calcul()
        discount_amount = total_price * (discount_percentage / 100)
        return total_price - discount_amount


def main():
    n = int(input())
    data = []
    for _ in range(n):
        for _ in range(6):
            data.append(input())
    
    cart = ShoppingCart()
    
    #print(data)

    i = 0
    for _ in range(n):
        type_product = data[i].strip()
        if type_product == 'book':
            id_product = data[i+1].strip()
            name_product = data[i+2].strip()
            price = data[i+3].strip()
            author = data[i+4].strip()
            product = Book(id_product, name_product, price, author)
            i += 5
        elif type_product == 'electronics':
            id_product = data[i+1].strip()
            name_product = data[i+2].strip()
            price = data[i+3].strip()
            manufacturer = data[i+4].strip()
            warranty_period = data[i+5].strip()
            product = Electronics(id_product, name_product, price, manufacturer, warranty_period)
            i += 6
        cart.product_add(product)
    
    for product in cart.products:
        print(product.info_get())
        print("---")
    
    total_before_discount = cart.total_calcul()
    discount_percentage = float(data[i].strip())
    total_after_discount = cart.discount_apply(discount_percentage)
    total_after_discount = round(total_after_discount, 4)

    if int(total_before_discount) == total_before_discount:
        total_before_discount = int(total_before_discount)

    if int(total_after_discount) == total_after_discount:
        total_after_discount = int(total_after_discount)

    print(f"Total price before discount: ${total_before_discount}")
    print(f"Total price after discount: ${total_after_discount}")


if __name__ == "__main__":
    main()
