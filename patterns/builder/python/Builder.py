from abc import ABC, abstractmethod

# Product
class House:
    def __init__(self):
        self.foundation = ""
        self.structure = ""
        self.roof = ""
        self.interior = ""

    def display(self):
        print("House with:")
        print(f"  Foundation: {self.foundation}")
        print(f"  Structure: {self.structure}")
        print(f"  Roof: {self.roof}")
        print(f"  Interior: {self.interior}")

# Builder interface
class HouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass

# Concrete Builder
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = "Concrete foundation"

    def build_structure(self):
        self.house.structure = "Wood and brick structure"

    def build_roof(self):
        self.house.roof = "Concrete roof"

    def build_interior(self):
        self.house.interior = "Modern interior"

    def get_house(self) -> House:
        return self.house

# Director
class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_interior()


if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = Director(builder)
    director.construct()
    house = builder.get_house()
    house.display()
