class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private variable
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# Create object
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Use getter method
print(my_tesla.get_brand())
 