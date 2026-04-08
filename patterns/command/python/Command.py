from abc import ABC, abstractmethod

# Receiver
class Light:
    def __init__(self, location: str):
        self.location = location

    def on(self) -> str:
        return f"{self.location} light is ON"

    def off(self) -> str:
        return f"{self.location} light is OFF"

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self) -> str:
        return self._light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self) -> str:
        return self._light.off()

# Invoker
class RemoteControl:
    def __init__(self):
        self._command: Command = None

    def set_command(self, command: Command):
        self._command = command

    def press_button(self) -> str:
        return self._command.execute()


if __name__ == "__main__":
    light = Light("Living Room")

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.set_command(light_on)
    print(remote.press_button())

    remote.set_command(light_off)
    print(remote.press_button())
