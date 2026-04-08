import copy
from abc import ABC, abstractmethod

# Prototype interface
class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass

# Concrete Prototype
class Document(Prototype):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def clone(self) -> "Document":
        return copy.copy(self)

    def get_info(self) -> str:
        return f"Document: {self.title} - {self.content}"


if __name__ == "__main__":
    # Original document
    original = Document("Original Document", "This is the original content")
    print(original.get_info())

    # Clone the document
    cloned = original.clone()
    cloned.title = "Cloned Document"
    cloned.content = "This is the cloned content"
    print(cloned.get_info())

    # Original remains unchanged
    print("Original after cloning:", original.get_info())
