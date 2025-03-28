class mahsool:
    def __init__(self, mahsool_id, mahsool_name, mahsool_price):
        self.mahsool_price = mahsool_price
        self.mahsool_name = mahsool_name
        self.mahsool_id = mahsool_id

    def get_info(self):
        output = "Product ID: {}\nName: {}\nPrice: ${}".format(self.mahsool_id, self.mahsool_name, self.mahsool_price)
        return output

class Book(mahsool):
    def __init__(self, mahsool_id, mahsool_name, mahsool_price, book_author):
        super().__init__(mahsool_id, mahsool_name, mahsool_price)
        self.book_author = book_author

    def get_info(self):
        output = super().get_info() + "\nAuthor: {}\n---".format(self.book_author)
        return output

class Store:
    def __init__(self):
        self.cart_items = []

    def add_mahsool(self, mahsool):
        self.cart_items.append(mahsool)

    def apply_discount(self, discount_percentage):
        total = 0 

        for mahsool in self.cart_items:
            total += mahsool.mahsool_price
            #print(total)
            #print(mahsool)
            #print(mahsool.mahsool_price)
        total_after_discount = total * (1 - discount_percentage / 100)

        print("Total price after discount: ${:.2f}".format(total_after_discount))

    def preview(self):
        for mahsool in self.cart_items:
            print(mahsool.get_info())

        total_before_discount = 0 
        for mahsool in self.cart_items:
            total_before_discount += mahsool.mahsool_price

        print("Total price before discount: ${:.2f}".format(total_before_discount))
        self.apply_discount(float(input()))

class Electronics(mahsool):
    def __init__(self, mahsool_id, mahsool_name, mahsool_price, mahsool_manufacturer, warranty_years):
        super().__init__(mahsool_id, mahsool_name, mahsool_price)
        self.mahsool_manufacturer = mahsool_manufacturer
        self.warranty_years = warranty_years

    def get_info(self):
        if self.warranty_years:
            warranty = "{} years".format(self.warranty_years)

        else:
            warranty = "NO WARRANTY"
        output = super().get_info() + "\nManufacturer: {}\nWarranty Period: {}\n---".format(self.mahsool_manufacturer, warranty)
        return output


object = Store()
for i in range(int(input())):
    mahsool_type = input()
    mahsool_id = input()

    if mahsool_type == 'book':
        mahsool_name = input()
        mahsool_price = float(input())
        book_author = input()
        object.add_mahsool(Book(mahsool_id, mahsool_name, mahsool_price, book_author))
    elif mahsool_type == 'electronics':
        mahsool_name = input()
        mahsool_price = float(input())
        mahsool_manufacturer = input()
        warranty_years = float(input())
        object.add_mahsool(Electronics(mahsool_id, mahsool_name, mahsool_price, mahsool_manufacturer, warranty_years))

object.preview()


