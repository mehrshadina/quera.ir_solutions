class kala:
    def __init__(self, kala_id, kala_name, gheymat_kala):
        self.gheymat_kala = gheymat_kala
        self.kala_name = kala_name
        self.kala_id = kala_id

    def get_info(self):
        return "Product ID: " + self.kala_id + "\nName: " + self.kala_name + "\nPrice: $" + self.gheymat_kala
    
class Book(kala):
    def __init__(self, kala_id, kala_name, gheymat_kala, nevisande):
        super().__init__(kala_id, kala_name, gheymat_kala)
        self.nevisande = nevisande

    def get_info(self):
        return super().get_info() + "\nAuthor: " + self.nevisande + "\n---"

class Store:
    def __init__(self):
        self.cart_items = []
    
    def apply_discount(self, discount_percentage):
        kol = 0 

        for kala in self.cart_items:
            kol += kala.gheymat_kala

        after_discount = kol * (1 - discount_percentage / 100)

        print("Total price after discount: ${:.2f}".format(after_discount))

    def add_kala(self, kala):
        self.cart_items.append(kala)


    def preview(self):
        for kala in self.cart_items:
            print(kala.get_info())

        before_discount = 0 
        for kala in self.cart_items:
            before_discount += kala.gheymat_kala

        print("Total price before discount: ${:.2f}".format(before_discount))
        self.apply_discount(float(input()))

class Electronics(kala):
    def __init__(self, kala_id, kala_name, gheymat_kala, kala, warranty_expire):
        super().__init__(
            kala_id, 
            kala_name, 
            gheymat_kala)
        
        self.warranty_expire = warranty_expire
        self.kala = kala

    def get_info(self):
        if not self.warranty_expire:
            warranty = "NO WARRANTY"
        elif self.warranty_expire:
            warranty = self.warranty_expire + " years"
        return super().get_info() + "\nManufacturer: " + self.kala + "\nWarranty Period: " + warranty + "\n---"

def elec(kala_type, kala_id):
    kala_name = input()
    gheymat_kala = float(input())

    kala = input()

    warranty_expire = float(input())

    shey.add_kala(
        Electronics(kala_id, kala_name, gheymat_kala, kala, warranty_expire)
        )


def ketab(kala_type, kala_id):
    kala_name = input()
    gheymat_kala = float(input())
    nevisande = input()
    shey.add_kala(
        Book(kala_id, kala_name, gheymat_kala, nevisande)
        )

shey = Store()
for i in range(int(input())):
    kala_type = input()
    kala_id = input()

    if kala_type == 'electronics':
        elec(kala_type, kala_id)
    
    elif kala_type == 'book':
        ketab(kala_type, kala_id)

shey.preview()


