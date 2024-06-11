class Car:

    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"Este coche ha recorrido {self.odometer_reading} Km")

    def get_descriptive_name(self):
        log_name = f"{self.year} {self.make} {self.model}"
        return log_name.title()

    def update_odometer(self,km):
        self.odometer_reading = km

    def increment_odometer(self,km):
        self.odometer_reading += km

audi = Car("Audi", "A4", "2024")
print(audi.get_descriptive_name())
audi.odometer_reading = 23
audi.read_odometer()

audi.update_odometer(50)
audi.increment_odometer(10)
audi.read_odometer()