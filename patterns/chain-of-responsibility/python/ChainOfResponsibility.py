from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Request
@dataclass
class SupportTicket:
    level: int
    message: str

# Handler interface
class SupportHandler(ABC):
    def __init__(self):
        self._next: SupportHandler = None

    def set_next(self, handler: SupportHandler) -> SupportHandler:
        self._next = handler
        return handler

    @abstractmethod
    def handle_request(self, ticket: SupportTicket) -> str:
        pass

# Base handling logic
class BaseHandler(SupportHandler):
    def handle_request(self, ticket: SupportTicket) -> str:
        if self._next:
            return self._next.handle_request(ticket)
        return "No handler available"

# Level 1 Support
class Level1Support(BaseHandler):
    def handle_request(self, ticket: SupportTicket) -> str:
        if ticket.level <= 1:
            return f"Level 1 Support: Handling ticket - {ticket.message}"
        return super().handle_request(ticket)

# Level 2 Support
class Level2Support(BaseHandler):
    def handle_request(self, ticket: SupportTicket) -> str:
        if ticket.level <= 2:
            return f"Level 2 Support: Handling ticket - {ticket.message}"
        return super().handle_request(ticket)

# Level 3 Support
class Level3Support(BaseHandler):
    def handle_request(self, ticket: SupportTicket) -> str:
        if ticket.level <= 3:
            return f"Level 3 Support: Handling ticket - {ticket.message}"
        return super().handle_request(ticket)


if __name__ == "__main__":
    level1 = Level1Support()
    level2 = Level2Support()
    level3 = Level3Support()

    level1.set_next(level2)
    level2.set_next(level3)

    tickets = [
        SupportTicket(level=1, message="Password reset"),
        SupportTicket(level=2, message="Software installation issue"),
        SupportTicket(level=3, message="Server crash investigation"),
    ]

    for ticket in tickets:
        print(level1.handle_request(ticket))
