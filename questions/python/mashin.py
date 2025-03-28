import csv

class Car:
    def __init__(self, car_id, brand, model, color, purchase_price, used_years=None, used_km=None, is_sold=False):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.color = color
        self.purchase_price = purchase_price
        self.used_years = used_years
        self.used_km = used_km
        self.is_new = used_years is None and used_km is None
        self.is_sold = is_sold

    def __str__(self):
        if self.is_new:
            return f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price} (new)"
        else:
            return f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price} | used years: {self.used_years} - {self.used_km}KM"

    def to_dict(self):
        return {
            'car_id': self.car_id,
            'brand': self.brand,
            'model': self.model,
            'color': self.color,
            'purchase_price': self.purchase_price,
            'used_years': self.used_years,
            'used_km': self.used_km,
            'is_new': self.is_new,
            'is_sold': self.is_sold
        }

class Dealership:
    def __init__(self):
        self.cars = []
        self.contracts = []
        self.load_data()

    def save_data(self):
        with open('cars.csv', 'w', newline='') as csvfile:
            fieldnames = ['car_id', 'brand', 'model', 'color', 'purchase_price', 'used_years', 'used_km', 'is_sold']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for car in self.cars:
                writer.writerow(car.to_dict())
        
        with open('contracts.csv', 'w', newline='') as csvfile:
            fieldnames = ['car_id', 'sale_price', 'buyer', 'benefit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contract in self.contracts:
                writer.writerow({
                    'car_id': contract[0],
                    'sale_price': contract[1],
                    'buyer': contract[2],
                    'benefit': contract[3]
                })

    def load_data(self):
        try:
            with open('cars.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.cars = [Car(int(row['car_id']), row['brand'], row['model'], row['color'], float(row['purchase_price']), int(row['used_years']) if row['used_years'] else None, float(row['used_km']) if row['used_km'] else None, row['is_sold'] == 'True') for row in reader]
                self.next_id = max(car.car_id for car in self.cars) + 1 if self.cars else 1001
        except FileNotFoundError:
            self.next_id = 1001
        
        try:
            with open('contracts.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.contracts = [(int(row['car_id']), float(row['sale_price']), row['buyer'], float(row['benefit'])) for row in reader]
        except FileNotFoundError:
            pass

    def add_new_car(self, brand, model, color, purchase_price):
        car = Car(self.next_id, brand, model, color, purchase_price)
        self.cars.append(car)
        self.next_id += 1
        #self.save_data()
        print("New car is successfully added.")

    def add_used_car(self, brand, model, color, purchase_price, used_years, used_km):
        car = Car(self.next_id, brand, model, color, purchase_price, used_years, used_km)
        self.cars.append(car)
        self.next_id += 1
        #self.save_data()
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
            #self.save_data()
            print(f"Car with ID: {car_id} is successfully saled.")

    def show_contracts(self):
        for car_id, sale_price, buyer, benefit in self.contracts:
            print(f"car with ID({car_id}) to {buyer} --> price: {sale_price} |benefit: {benefit}|")

    def process_command(self, command):
        parts = command.split()

        if not parts:
            print("Invalid command!")
            return
        cmd = ' '.join(parts[:3])

        if cmd == "Help":
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
        elif cmd == "Purchase new car":
            self.add_new_car(parts[3], parts[4], parts[5], int(parts[6]))
        elif cmd == "Purchase used car":
            self.add_used_car(parts[3], parts[4], parts[5], int(parts[6]), int(parts[7]), int(parts[8]))
        elif cmd == "Show available cars":
            self.show_available_cars()
        elif cmd == "Show available new":
            self.show_available_new_cars()
        elif cmd == "Show available used":
            self.show_available_used_cars()
        elif cmd.startswith("Sale car"):
            self.sale_car(int(parts[2]), int(parts[3]), parts[4])
        elif cmd == "Show contracts":
            self.show_contracts()
        elif cmd.startswith("Exit"):
            print("Good luck...")
            exit()
        else:
            print("Invalid command!")

dealership = Dealership()
while True:
    command = input().strip()
    dealership.process_command(command)


