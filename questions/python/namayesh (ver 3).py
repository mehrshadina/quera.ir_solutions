class Car:
    def __init__(self, car_id, brand, model, color, purchase_price, used_years=None, used_km=None):
        self.car_id = car_id
        self.purchase_price = purchase_price
        self.used_years = used_years
        self.used_km = used_km
        self.brand = brand
        self.model = model
        self.color = color
        self.is_new = used_years is None and used_km is None
        self.is_sold = False

    def __str__(self):
        info = f"{self.brand} {self.model} {self.color} -{self.car_id}- purchase price: {self.purchase_price}"
        if self.is_new:
            return f"{info} (new)"
        else:
            return f"{info} | used years: {self.used_years} - {self.used_km}KM"

class Dealership:
    def __init__(self):
        self.next_id = 1001
        self.cars = []
        self.contracts = []

    def add_new_car(self, brand, model, color, purchase_price):
        car = Car(self.next_id, brand, model, color, purchase_price)
        self.cars.append(car)
        self.next_id += 1
        
    def sale_car(self, car_id, sale_price, buyer):
        car = next((c for c in self.cars if c.car_id == car_id and not c.is_sold), None)
        if car is None:
            print("Car with this ID is not found!")
        else:
            car.is_sold = True
            benefit = sale_price - car.purchase_price
            self.contracts.append((car_id, sale_price, buyer, benefit))
            print(f"Car with ID: {car_id} is successfully saled.")
    
    def add_used_car(self, brand, model, color, purchase_price, used_years, used_km):
        car = Car(self.next_id, brand, model, color, purchase_price, used_years, used_km)
        self.cars.append(car)
        self.next_id += 1

    def main(self):
        while True:
            command = input().strip()
            self.process_command(command)
    
    def show_contracts(self):
        for car_id, sale_price, buyer, benefit in self.contracts:
            print(f"car with ID({car_id}) to {buyer} --> price: {sale_price} |benefit: {benefit}|")

    def process_command(self, command):
        parts = command.split()
        if not parts:
            print("Invalid command!")
            return
        cmd = parts[0]
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
        elif cmd == "Show" and parts[1] == "contracts":
            self.show_contracts()
        elif cmd == "Purchase" and len(parts) == 9:
            self.add_used_car(
                parts[3], parts[4], parts[5], int(parts[6]), int(parts[7]), int(parts[8]))
            print("New used car is successfully added.")
        elif cmd == "Purchase" and len(parts) == 7: 
            self.add_new_car(
                parts[3], parts[4], parts[5], int(parts[6]))
            print("New car is successfully added.")
        elif cmd == "Sale" and len(parts) == 5 and parts[1] == "car":
            self.sale_car(
                int(parts[2]), int(parts[3]), parts[4])
        elif cmd == "Show" and parts[1] == "available":
            if parts[2] == "cars":
                for car in self.cars:
                    if not car.is_sold and car.is_new:
                        print(str(car)[:-6])
            elif parts[2] == "new" and parts[3] == "cars":
                for car in self.cars:
                    if not car.is_sold and car.is_new:
                        print(str(car)[:-6])
            elif parts[2] == "used" and parts[3] == "cars":
                for car in self.cars:
                    if not car.is_sold and car.is_new:
                        print(str(car)[:-6])
            else:
                print("Invalid command!")
        elif cmd == "Exit":
            print("Good luck...")
            exit()
        else:
            print("Invalid command!")


if __name__ == "__main__":
    dell = Dealership()
    dell.main()
