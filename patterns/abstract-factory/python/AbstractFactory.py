from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Concrete Products - Windows
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering Windows Button"

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Windows Checkbox"

# Concrete Products - Mac
class MacButton(Button):
    def render(self) -> str:
        return "Rendering Mac Button"

class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Mac Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory - Windows
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory - Mac
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


if __name__ == "__main__":
    # Using Windows Factory
    factory: GUIFactory = WindowsFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

    # Using Mac Factory
    factory = MacFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())
