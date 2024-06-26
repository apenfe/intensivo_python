from car import Car

class Battery:

    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a battery of {self.battery_size}")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 255

        print(f"This car has a battery of {range} km range")

class ElectricCar(Car):

    def __init__(self,make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Este coche no usa gasolina")

my_leaf = ElectricCar('Tesla','X',2020)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()