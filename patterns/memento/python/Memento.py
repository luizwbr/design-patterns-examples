from typing import List

# Memento
class Memento:
    def __init__(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content

# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def set_content(self, content: str):
        self._content = content

    def get_content(self) -> str:
        return self._content

    def save(self) -> Memento:
        return Memento(self._content)

    def restore(self, memento: Memento):
        self._content = memento.get_content()

# Caretaker
class History:
    def __init__(self):
        self._mementos: List[Memento] = []

    def push(self, memento: Memento):
        self._mementos.append(memento)

    def pop(self) -> Memento:
        if not self._mementos:
            return None
        return self._mementos.pop()


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.set_content("Version 1")
    history.push(editor.save())
    print("Current:", editor.get_content())

    editor.set_content("Version 2")
    history.push(editor.save())
    print("Current:", editor.get_content())

    editor.set_content("Version 3")
    print("Current:", editor.get_content())

    # Undo to Version 2
    editor.restore(history.pop())
    print("After undo:", editor.get_content())

    # Undo to Version 1
    editor.restore(history.pop())
    print("After undo:", editor.get_content())
