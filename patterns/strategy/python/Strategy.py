from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self._card_number = card_number

    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Credit Card ending in {self._card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self._email = email

    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal account {self._email}"

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self._wallet_address = wallet_address

    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Bitcoin wallet {self._wallet_address[:8]}..."

# Context
class ShoppingCart:
    def __init__(self, amount: float):
        self._amount = amount
        self._payment_strategy: PaymentStrategy = None

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self._payment_strategy = strategy

    def checkout(self) -> str:
        return self._payment_strategy.pay(self._amount)


if __name__ == "__main__":
    cart = ShoppingCart(100.0)

    cart.set_payment_strategy(CreditCardPayment("1234567890123456"))
    print(cart.checkout())

    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    print(cart.checkout())

    cart.set_payment_strategy(BitcoinPayment("1A2B3C4D5E6F7G8H"))
    print(cart.checkout())
