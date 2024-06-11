class Car:

    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        log_name = f"{self.year} {self.make} {self.model}"
        return log_name.title()

audi = Car("Audi", "A4", "2024")
print(audi.get_descriptive_name())