class Automobile:
    def __init__(self, car_id, brand, model, color, purchase_price, used_years=None, used_km=None):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.color = color
        self.purchase_price = purchase_price
        self.used_years = used_years
        self.used_km = used_km
        self.is_new = used_years is None and used_km is None
        self.is_sold = False
        self.maintenance_records = []

    def __str__(self):
        if self.is_new:
            return f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price} (new)"
        else:
            return f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price} | used years: {self.used_years} - {self.used_km}KM"

    def add_maintenance(self, date, description, cost):
        self.maintenance_records.append({"date": date, "description": description, "cost": cost})
        print(f"Added maintenance record on {date} for {description} costing {cost}")

    def show_maintenance(self):
        print(f"Maintenance records for {self.brand} {self.model} {self.color} -{self.car_id}-")
        for record in self.maintenance_records:
            print(f"Date: {record['date']}, Description: {record['description']}, Cost: {record['cost']}")

class Program:
    def __init__(self):
        self.cars = []
        self.next_id = 1001
        self.contracts = []

    def add_new_car(self, brand, model, color, purchase_price):
        car = Automobile(self.next_id, brand, model, color, purchase_price)
        self.cars.append(car)
        self.next_id += 1
        print("New car is successfully added.")

    def add_used_car(self, brand, model, color, purchase_price, used_years, used_km):
        car = Automobile(self.next_id, brand, model, color, purchase_price, used_years, used_km)
        self.cars.append(car)
        self.next_id += 1
        print("New used car is successfully added.")

    def show_available_cars(self):
        for car in self.cars:
            if not car.is_sold:
                print(car)

    def show_available_new_cars(self):
        for car in self.cars:
            if not car.is_sold and car.is_new:
                print(str(car)[:-5])

    def show_available_used_cars(self):
        for car in self.cars:
            if not car.is_sold and not car.is_new:
                print(car)

    def sale_car(self, car_id, sale_price, buyer):
        car = next((c for c in self.cars if c.car_id == car_id and not c.is_sold), None)
        if car is None:
            print("Car with this ID is not found!")
        else:
            car.is_sold = True
            benefit = sale_price - car.purchase_price
            self.contracts.append((car_id, sale_price, buyer, benefit))
            print(f"Car with ID: {car_id} is successfully saled.")

    def show_contracts(self):
        for car_id, sale_price, buyer, benefit in self.contracts:
            print(f"car with ID({car_id}) to {buyer} --> price: {sale_price} |benefit: {benefit}|")

    def process(self, command):
        parts = command.split()
        inputt = ' '.join(parts[:3])
        if inputt == "Help":
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
        elif inputt == "Purchase new car":
            self.add_new_car(parts[3].strip(), parts[4].strip(), parts[5].strip(), int(parts[6].strip()))
        elif inputt == "Purchase used car":
            self.add_used_car(parts[3].strip(), parts[4].strip(), parts[5].strip(), int(parts[6].strip()), int(parts[7].strip()), int(parts[8].strip()))
        elif inputt.startswith("Sale car"):
            self.sale_car(int(parts[2].strip()), int(parts[3].strip()), parts[4].strip())
        elif inputt == "Show contracts":
            self.show_contracts()
        elif inputt == "Add maintenance":
            car_id = int(parts[1].strip())
            car = next((c for c in self.cars if c.car_id == car_id), None)
            if car:
                car.add_maintenance(parts[2].strip(), parts[3].strip(), float(parts[4].strip()))
            else:
                print("Car with this ID is not found!")
        elif inputt == "Show maintenance":
            car_id = int(parts[1].strip())
            car = next((c for c in self.cars if c.car_id == car_id), None)
            if car:
                car.show_maintenance()
            else:
                print("Car with this ID is not found!")
        elif inputt == "Show available cars":
            self.show_available_cars()
        elif inputt == "Show available new":
            self.show_available_new_cars()
        elif inputt == "Show available used":
            self.show_available_used_cars()
        elif inputt == "Exit":
            print("Good luck...")
            exit()
        else:
            print("Invalid command!")

def main():
    Mainprogram = Program()
    while True:
        command = input().strip()
        Mainprogram.process(command)


main()
