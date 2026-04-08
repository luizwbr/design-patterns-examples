from abc import ABC, abstractmethod

# Product interface
class Vehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

# Concrete Products
class Car(Vehicle):
    def drive(self) -> str:
        return "Driving a car on the road"

class Bike(Vehicle):
    def drive(self) -> str:
        return "Riding a bike on the path"

# Creator interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

# Concrete Creators
class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()


if __name__ == "__main__":
    # Using Car Factory
    car_factory = CarFactory()
    car = car_factory.create_vehicle()
    print(car.drive())

    # Using Bike Factory
    bike_factory = BikeFactory()
    bike = bike_factory.create_vehicle()
    print(bike.drive())
