from abc import ABC, abstractmethod
from typing import List

# Component interface
class Employee(ABC):
    @abstractmethod
    def show_details(self) -> str:
        pass

# Leaf
class Developer(Employee):
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def show_details(self) -> str:
        return f"{self.name} - {self.position}"

# Composite
class Manager(Employee):
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        self._subordinates: List[Employee] = []

    def add(self, employee: Employee):
        self._subordinates.append(employee)

    def remove(self, employee: Employee):
        self._subordinates.remove(employee)

    def show_details(self) -> str:
        result = f"{self.name} - {self.position}\n"
        for employee in self._subordinates:
            result += "  " + employee.show_details() + "\n"
        return result


if __name__ == "__main__":
    dev1 = Developer("John", "Frontend Developer")
    dev2 = Developer("Jane", "Backend Developer")

    manager = Manager("Bob", "Engineering Manager")
    manager.add(dev1)
    manager.add(dev2)

    print(manager.show_details())
