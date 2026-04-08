from __future__ import annotations
from abc import ABC, abstractmethod

# State interface
class DocumentState(ABC):
    @abstractmethod
    def publish(self, doc: "Document") -> str:
        pass

    @abstractmethod
    def review(self, doc: "Document") -> str:
        pass

# Context
class Document:
    def __init__(self, name: str):
        self.name = name
        self._state: DocumentState = DraftState()

    def set_state(self, state: DocumentState):
        self._state = state

    def publish(self) -> str:
        return self._state.publish(self)

    def review(self) -> str:
        return self._state.review(self)

# Concrete States
class DraftState(DocumentState):
    def publish(self, doc: Document) -> str:
        return "Cannot publish from Draft. Please review first."

    def review(self, doc: Document) -> str:
        doc.set_state(ReviewState())
        return "Document moved to Review state"

class ReviewState(DocumentState):
    def publish(self, doc: Document) -> str:
        doc.set_state(PublishedState())
        return "Document published successfully"

    def review(self, doc: Document) -> str:
        return "Document is already in Review state"

class PublishedState(DocumentState):
    def publish(self, doc: Document) -> str:
        return "Document is already published"

    def review(self, doc: Document) -> str:
        return "Cannot review a published document"


if __name__ == "__main__":
    doc = Document("Design Patterns Guide")

    print("Initial state: Draft")
    print(doc.publish())
    print(doc.review())
    print(doc.publish())
