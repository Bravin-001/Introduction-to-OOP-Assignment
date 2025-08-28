# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Example usage
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())