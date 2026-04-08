from typing import List

# Subsystem: CPU
class CPU:
    def freeze(self) -> str:
        return "CPU: Freezing processor"

    def jump(self, position: str) -> str:
        return f"CPU: Jumping to position {position}"

    def execute(self) -> str:
        return "CPU: Executing instructions"

# Subsystem: Memory
class Memory:
    def load(self, position: str, data: str) -> str:
        return f"Memory: Loading '{data}' at position {position}"

# Subsystem: HardDrive
class HardDrive:
    def read(self, sector: str, size: str) -> str:
        return f"HardDrive: Reading {size} bytes from sector {sector}"

# Facade
class ComputerFacade:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hard_drive = HardDrive()

    def start(self) -> List[str]:
        results = []
        results.append("Starting Computer...")
        results.append(self._cpu.freeze())
        results.append(self._memory.load("0x00", "BOOT_ADDRESS"))
        results.append(self._hard_drive.read("0", "1024"))
        results.append(self._cpu.jump("0x00"))
        results.append(self._cpu.execute())
        results.append("Computer started successfully!")
        return results


if __name__ == "__main__":
    computer = ComputerFacade()
    for result in computer.start():
        print(result)
