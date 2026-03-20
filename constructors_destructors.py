class Car:
    def __init__(self, brand, year, make):
        self.brand = brand
        self.year = year
        self.make = make


    def show(self):
        print(f"Car brand: {self.brand}, Year: {self.year}, Make: {self.make}")


car1 = Car("Toyota", 2020, "Camry")

car1.show()