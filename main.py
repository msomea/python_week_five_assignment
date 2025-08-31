# Assignment 1
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call the base class constructor
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f"Calling {number} from {self.device_info()}..."

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        return f"Battery charged to {self.battery}%"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 50)
phone2 = Smartphone("Apple", "iPhone 15", "512GB", 80)

# Using methods
print(phone1.call("+123456789"))
print(phone2.charge(15))

# Assignment 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
