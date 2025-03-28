class Car:
    def __init__(self, car_id, brand, model, color, purchase_price, used_years=None, used_km=None):
        self.car_id = car_id
        self.brand = brand
        self.used_years = used_years
        self.used_km = used_km
        self.is_new = used_years is None and used_km is None
        self.is_sold = False
        self.model = model
        self.color = color
        self.purchase_price = purchase_price

    def __str__(self):
        text = f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price}"
        if self.is_new:
            return f"{text} (new)"
        else:
            return f"{text} | used years: {self.used_years} - {self.used_km}KM"

class Deal:
    def __init__(self):
        self.cars = []
        self.contracts = []
        self.next_id = 1001

    def add_new_car(self, brand, model, color, purchase_price):
        car = Car(self.next_id, brand, model, color, purchase_price)
        self.cars.append(car)
        print("New car is successfully added.")
        self.next_id += 1

    def add_used_car(self, brand, 
                     model, color, purchase_price, used_years, used_km):
        car = Car(self.next_id, brand, 
                  model, color, purchase_price, used_years, used_km)
        self.cars.append(car)
        print("New used car is successfully added.")
        self.next_id += 1

    def show_available_cars(self):
        for car in self.cars:
            if not car.is_sold:
                print(car)

    def show_new(self):
        for car in self.cars:
            if car.is_new:
                if not car.is_sold: 
                    print(str(car)[:-6])

    def show_used(self):
        for car in self.cars:
            if not car.is_new:
                if not car.is_sold: 
                    print(car)

    def show_contracts(self):
        for car_id, sale_price, buyer, benefit in self.contracts:
            print(f"car with ID({car_id}) to {buyer} --> price: {sale_price} |benefit: {benefit}|")
   
    def sale_car(self, car_id, sale_price, buyer):
        car = next((c for c in self.cars if c.car_id == car_id and not c.is_sold), None)
        if car is None:
            print("Car with this ID is not found!")
        else:
            car.is_sold = True
            benefit = sale_price - car.purchase_price
            self.contracts.append((car_id, sale_price, buyer, benefit))
            print(f"Car with ID: {car_id} is successfully saled.")


    def process_command(self, command):
        parts = command.split()
        if not parts:
            print("Invalid command!")
            return
        cccccmm = parts[0]
        if cccccmm == "Help":
            print(
                "orders:\n"
                "Help\n"
                "Purchase new car |brand| |model| |color| |purchase price|\n"
                "Purchase used car |brand| |model| |color| |purchase price| |used years| |used KM|\n"
                "Show available cars\n"
                "Show available new cars\n"
                "Show available used cars\n"
                "Sale car |car ID| |price| |buyer|\n"
                "Show contracts\n"
                "Exit"
            )
        elif cccccmm == "Purchase" and len(parts) == 7:
            self.add_new_car(parts[3], parts[4], 
                             parts[5], int(parts[6]))
        elif cccccmm == "Purchase" and len(parts) == 9:
            self.add_used_car(parts[3], parts[4], parts[5], 
                              int(parts[6]), int(parts[7]), int(parts[8]))
        elif cccccmm == "Show" and parts[1] == "available":
            if parts[2] == "cars":
                self.show_available_cars()
            elif parts[2] == "new" and parts[3] == "cars":
                self.show_new()
            elif parts[2] == "used" and parts[3] == "cars":
                self.show_used()
            else:
                print("Invalid command!")
        elif cccccmm == "Sale" and len(parts) == 5 and parts[1] == "car":
            self.sale_car(int(parts[2]), int(parts[3]), 
                          parts[4])
        elif cccccmm == "Show" and parts[1] == "contracts":
            self.show_contracts()
        elif cccccmm == "Exit":
            print("Good luck...")
            exit()
        else:
            print("Invalid command!")


Deal1 = Deal()
while True:
    command = input().strip()
    Deal1.process_command(command)