from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temp: float):
        self._temperature = temp
        self.notify()

# Concrete Observers
class PhoneDisplay(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, temperature: float):
        print(f"{self.name}: Temperature updated to {temperature:.1f}°C")

class WindowDisplay(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, temperature: float):
        print(f"{self.name}: Temperature updated to {temperature:.1f}°C")


if __name__ == "__main__":
    station = WeatherStation()

    phone = PhoneDisplay("Phone Display")
    window = WindowDisplay("Window Display")

    station.attach(phone)
    station.attach(window)

    station.set_temperature(25.5)
    station.set_temperature(30.0)
