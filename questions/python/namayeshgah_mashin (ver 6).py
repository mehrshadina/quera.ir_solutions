class Car:
    def __init__(self, car_id, brand, model, color, purchase_price, new):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.color = color
        self.purchase_price = purchase_price
        self.is_sold = False
        self.new = new

    def __str__(self):
        return f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price}"

class NewCar(Car):
    def __init__(self, car_id, brand, model, color, purchase_price):
        super().__init__(car_id, brand, model, color, purchase_price, True)

    def __str__(self):
        return super().__str__()

class UsedCar(Car):
    def __init__(self, car_id, brand, model, color, purchase_price, used_years, used_km):
        super().__init__(car_id, brand, model, color, purchase_price, False)
        self.used_years = used_years
        self.used_km = used_km

    def __str__(self):
        return super().__str__() + f" | used years: {self.used_years} - {self.used_km}KM"

class Dealership:
    def __init__(self):
        self.cars = []
        self.next_id = 1001
        self.contracts = []

    def add_car(self, car):
        self.cars.append(car)
        self.next_id += 1
        print(f"{'New' if isinstance(car, NewCar) else 'New used'} car is successfully added.")

    def show_available_cars(self):
        for car in self.cars:
            if not car.is_sold:
                if car.new:
                    print(car, '(new)')
                else:
                    print(car)

    def show_available_new_cars(self):
        for car in self.cars:
            if not car.is_sold and car.new:
                print(car)

    def show_available_used_cars(self):
        for car in self.cars:
            if not car.is_sold and not car.new:
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

    def process_command(self, command):
        parts = command.split()
        #print(parts)
        if not parts:
            print("Invalid command!")
            return
        cmd = ' '.join(parts[:3])
        #print(cmd)
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
            self.add_car(NewCar(self.next_id, parts[3], parts[4], parts[5], int(parts[6])))
        elif cmd == "Purchase used car":
            self.add_car(UsedCar(self.next_id, parts[3], parts[4], parts[5], int(parts[6]), int(parts[7]), int(parts[8])))
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

