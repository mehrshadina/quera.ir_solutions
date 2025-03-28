class Car:
    def __init__(self, car_id, brand, model, color, purchase_price, used_years=None, used_km=None):
        self.purchase_price = purchase_price
        self.used_years = used_years
        self.used_km = used_km
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.color = color
        self.is_sold = False
        self.is_new = used_km is None and used_years is None

    def __str__(self):
        base_info = "{} {} {} -{}- purchase price: {}".format(
            self.brand, self.model, self.color, self.car_id, self.purchase_price)
        
        if self.is_new:
            return base_info + " (new)"
        else:
            return base_info + " | used years: " + str(self.used_years) + " - " + str(self.used_km) + "KM"

class Shop:
    def __init__(self):
        self.cars = []
        self.contracts = []
        self.next_id = 1001

    def add_new_car(self, command):
        parts = command.split()
    
        car = Car(
            self.next_id, 
            parts[3], 
            parts[4], 
            parts[5], 
            int(parts[6]))
        self.cars.append(car)
        self.next_id += 1
        

    def add_used_car(self, command):
        parts = command.split()
        car = Car(
            self.next_id, parts[3], 
            parts[4], 
            parts[5], 
            int(parts[6]), 
            int(parts[7]), 
            int(parts[8]))
        self.cars.append(car)
        self.next_id += 1
        

    def a_cars(self):
        for automobile in self.cars:
            if not automobile.is_sold:
                print(automobile)

    def a_new_cars(self):
        for automobile in self.cars:
            if not automobile.is_sold:
                if automobile.is_new:
                    print(str(automobile)[:-6])

    def a_used_cars(self):
        for automobile in self.cars:
            if not automobile.is_sold:
                if not automobile.is_new:
                    print(automobile)

    def sale_car(self, command):
        parts = command.split()
        car = next(
            (c for c in self.cars if c.car_id == int(parts[2]) and not c.is_sold),
            None)
        if car:
            car.is_sold = True
            benefit = int(parts[3]) - car.purchase_price
            self.contracts.append((int(parts[2]), int(parts[3]), parts[4], benefit))
            print("Car with ID: {} is successfully saled.".format(int(parts[2]))) # saled is gramitically wrong! we must say sold.
        else:
            print("Car with this ID is not found!")

    def factor(self):
        for car_id, sale_price, buyer, benefit in self.contracts:
            print(f"car with ID({car_id}) to {buyer} --> price: {sale_price} |benefit: {benefit}|")

    def show_help(self):
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

    def make_decision(self, command):
        parts = command.split()
        shell = parts[0]

        if shell == "Help":
            self.show_help()

        elif shell == "Purchase":
            if len(parts) == 7:
                self.add_new_car(command)
                print("New car is successfully added.")

            elif len(parts) == 9:
                self.add_used_car(command)
                print("New used car is successfully added.")

            else:
                print("Invalid command!")

        elif shell == "Show":
            if parts[1] == "available":
                if parts[2] == "cars":
                    self.a_cars()

                elif parts[2] == "new" and parts[3] == "cars":
                    self.a_new_cars()

                elif parts[2] == "used" and parts[3] == "cars":
                    self.a_used_cars()

                else:
                    print("Invalid command!")

            elif parts[1] == "contracts":
                self.factor()

        elif shell == "Sale":
            if parts[1] == "car":
                self.sale_car(command)
            
        elif shell == "Exit":
            print("Good luck...")
            exit()

        else:
            print("Invalid command!")

sss = Shop()
while True:
    command = input().strip()
    sss.make_decision(command)

