from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def get_description(self) -> str:
        return "Simple Coffee"

    def get_cost(self) -> float:
        return 2.0

# Decorator base
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_description(self) -> str:
        return self._coffee.get_description()

    def get_cost(self) -> float:
        return self._coffee.get_cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Sugar"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.3


if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"{coffee.get_description()}: ${coffee.get_cost():.2f}")

    coffee_with_milk = MilkDecorator(coffee)
    print(f"{coffee_with_milk.get_description()}: ${coffee_with_milk.get_cost():.2f}")

    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"{coffee_with_milk_and_sugar.get_description()}: ${coffee_with_milk_and_sugar.get_cost():.2f}")
