from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + Car.CONDITIONER_ON) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6

    def drive(self, distance):
        consumption = (self.fuel_consumption + Truck.CONDITIONER_ON) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)