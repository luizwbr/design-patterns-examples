from typing import Dict

# Flyweight: Character formatting (intrinsic state)
class CharacterFormat:
    def __init__(self, font: str, size: int, color: str):
        self.font = font
        self.size = size
        self.color = color

    def display(self, char: str) -> str:
        return f"Character '{char}' [Font: {self.font}, Size: {self.size}, Color: {self.color}]"

# Flyweight Factory
class FormatFactory:
    def __init__(self):
        self._formats: Dict[str, CharacterFormat] = {}

    def get_format(self, font: str, size: int, color: str) -> CharacterFormat:
        key = f"{font}-{size}-{color}"
        if key not in self._formats:
            self._formats[key] = CharacterFormat(font, size, color)
            print(f"Created new format: {key}")
        return self._formats[key]

    def get_total_formats(self) -> int:
        return len(self._formats)

# Character with extrinsic state
class Character:
    def __init__(self, char: str, fmt: CharacterFormat):
        self.char = char
        self.format = fmt

    def display(self) -> str:
        return self.format.display(self.char)

# Text Editor
class TextEditor:
    def __init__(self):
        self._characters = []
        self._factory = FormatFactory()

    def add_character(self, char: str, font: str, size: int, color: str):
        fmt = self._factory.get_format(font, size, color)
        self._characters.append(Character(char, fmt))

    def display(self):
        for char in self._characters:
            print(char.display())
        print(f"Total unique formats: {self._factory.get_total_formats()}")


if __name__ == "__main__":
    editor = TextEditor()

    # Adding characters with different formats
    editor.add_character("H", "Arial", 12, "Red")
    editor.add_character("e", "Arial", 12, "Red")
    editor.add_character("l", "Arial", 12, "Red")
    editor.add_character("l", "Times", 14, "Blue")
    editor.add_character("o", "Times", 14, "Blue")

    editor.display()
