from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Mediator interface
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: "User"):
        pass

    @abstractmethod
    def add_user(self, user: "User"):
        pass

# Concrete Mediator
class ChatRoom(ChatMediator):
    def __init__(self):
        self._users: List[User] = []

    def add_user(self, user: "User"):
        self._users.append(user)

    def send_message(self, message: str, sender: "User"):
        for user in self._users:
            if user is not sender:
                user.receive(message, sender.name)

# User
class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self._mediator = mediator
        self._messages: List[str] = []
        mediator.add_user(self)

    def send(self, message: str):
        print(f"{self.name} sends: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str, from_user: str):
        msg = f"{self.name} receives from {from_user}: {message}"
        self._messages.append(msg)
        print(msg)


if __name__ == "__main__":
    chat_room = ChatRoom()

    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)

    alice.send("Hello everyone!")
    bob.send("Hi Alice!")
    charlie.send("Hey folks!")
