from abc import ABC, abstractmethod
from typing import List

# Abstract class (template)
class Beverage(ABC):
    # Template method — defines the algorithm skeleton
    def prepare_recipe(self) -> List[str]:
        steps = []
        steps.append("Boiling water")
        steps.append(self.brew())
        steps.append("Pouring into cup")
        steps.append(self.add_condiments())
        return steps

    @abstractmethod
    def brew(self) -> str:
        pass

    @abstractmethod
    def add_condiments(self) -> str:
        pass

# Concrete implementations
class Tea(Beverage):
    def brew(self) -> str:
        return "Steeping the tea"

    def add_condiments(self) -> str:
        return "Adding lemon"

class Coffee(Beverage):
    def brew(self) -> str:
        return "Dripping coffee through filter"

    def add_condiments(self) -> str:
        return "Adding sugar and milk"


if __name__ == "__main__":
    print("Making tea:")
    tea = Tea()
    for step in tea.prepare_recipe():
        print(f"- {step}")

    print("\nMaking coffee:")
    coffee = Coffee()
    for step in coffee.prepare_recipe():
        print(f"- {step}")
